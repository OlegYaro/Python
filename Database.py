import sqlite3 as sq
from parser import Parser
from Transaction import Transaction

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