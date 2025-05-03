import sys
import sqlite3 as sq
import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtCore as QtCore
from parser import Parser


class Transaction:
    def __init__(self, name, price, amount, operation, date):
        self.name = name
        self.price = price
        self.amount = amount
        self.operation = operation
        self.date = date

    def process(self):
        return (self.name, self.price, self.amount, self.operation, self.date)

class Database:
    def __init__(self):
        self.con = sq.connect("portfolio.db")
        self.cur = self.con.cursor()
        self.parser_data = None

    def create_table(self):
        with self.con:
            self.cur.execute("""CREATE TABLE IF NOT EXISTS portfolio (
                name TEXT,
                price REAL,
                amount REAL,
                operation INTEGER,
                date REAL
            )""")

    def add_transaction(self, name, price, amount, operation, date):
        transaction = Transaction(name, price, amount, operation, date)
        with self.con:
            self.cur.execute("INSERT INTO portfolio VALUES (?, ?, ?, ?, ?)", transaction.process())

    def update_prices(self):
        self.cur.execute("SELECT DISTINCT name FROM portfolio")
        coins = [row[0] for row in self.cur.fetchall()]
        parser = Parser()
        self.parser_data = {coin: parser.get_price(coin) for coin in coins}

    def get_summary(self):
        self.cur.execute("SELECT DISTINCT name FROM portfolio")
        coins = [row[0] for row in self.cur.fetchall()]

        summary = ""
        total_invested = 0

        for coin in coins:
            self.cur.execute("SELECT * FROM portfolio WHERE name=?", (coin,))
            records = self.cur.fetchall()

            quantity = 0
            total_buy_price = 0
            total_sell_price = 0
            total_price = 0
            buy_volume = 0
            sell_volume = 0

            for record in records:
                amount = float(str(record[2]).replace(',', '.'))
                price = float(str(record[1]).replace(',', '.'))
                operation = record[3]

                if operation == 1:
                    quantity += amount
                    total_buy_price += price
                    total_price += price
                    buy_volume += amount
                elif operation == 2:
                    quantity -= amount
                    total_sell_price += price
                    total_price -= price
                    sell_volume += amount

            current_price = self.parser_data.get(coin, 0)
            current_value = current_price * quantity
            pnl = current_value - total_price
            total_invested += total_price

            avg_buy = total_buy_price / buy_volume if buy_volume else 0
            avg_sell = total_sell_price / sell_volume if sell_volume else 0

            summary += (
                f"Coin: {coin}\n"
                f"Quantity: {quantity}\n"
                f"Current Price: ${current_price:.6f}\n"
                f"Avg Buy Price: ${avg_buy:.6f}\n"
                f"Avg Sell Price: ${avg_sell:.6f}\n"
                f"Total Invested: ${total_price:.2f}\n"
                f"Current Value: ${current_value:.2f}\n"
                f"PnL: ${pnl:.2f}\n\n"
            )

        return summary

    def __del__(self):
        self.con.close()
        print("Database connection closed")

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.db.create_table()

        self.setWindowTitle("Crypto Portfolio")
        self.setGeometry(100, 100, 600, 500)

        layout = QtWidgets.QVBoxLayout(self)

        form_layout = QtWidgets.QFormLayout()
        self.name_entry = QtWidgets.QLineEdit()
        self.price_entry = QtWidgets.QLineEdit()
        self.amount_entry = QtWidgets.QLineEdit()
        self.operation_entry = QtWidgets.QLineEdit()
        self.date_entry = QtWidgets.QLineEdit()

        form_layout.addRow("Coin Name", self.name_entry)
        form_layout.addRow("Price", self.price_entry)
        form_layout.addRow("Amount", self.amount_entry)
        form_layout.addRow("Operation (1=Buy, 2=Sell)", self.operation_entry)
        form_layout.addRow("Date", self.date_entry)

        layout.addLayout(form_layout)

        self.add_btn = QtWidgets.QPushButton("Add Transaction")
        self.add_btn.clicked.connect(self.add_transaction)
        layout.addWidget(self.add_btn)

        self.output_btn = QtWidgets.QPushButton("Show Summary")
        self.output_btn.clicked.connect(self.display_summary)
        layout.addWidget(self.output_btn)

        self.output_text = QtWidgets.QTextEdit()
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

    def add_transaction(self):
        try:
            name = self.name_entry.text()
            price = float(self.price_entry.text())
            amount = float(self.amount_entry.text())
            operation = int(self.operation_entry.text())
            date = float(self.date_entry.text())

            if name and price and amount and operation and date:
                self.db.add_transaction(name, price, amount, operation, date)
                QtWidgets.QMessageBox.information(self, "Success", "Transaction added successfully!")
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "All fields are required!")
        except ValueError:
            QtWidgets.QMessageBox.critical(self, "Error", "Invalid input values")

    def display_summary(self):
        self.db.update_prices()
        summary = self.db.get_summary()
        self.output_text.setPlainText(summary)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
