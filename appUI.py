import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtCore as QtCore
from Database import Database


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.db.create_table()

        self.setWindowTitle("Crypto Portfolio")
        self.setGeometry(100, 100, 702, 782)

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
