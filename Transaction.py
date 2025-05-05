class Transaction:
    def __init__(self, name, price, amount, operation, date):
        self.name = name
        self.price = price
        self.amount = amount
        self.operation = operation
        self.date = date

    def process(self):
        return (self.name, self.price, self.amount, self.operation, self.date)