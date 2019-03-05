class BankAccount:
    number = 0
    cash = 0.0
    def __init__(self, number):
        self.number = number
        self.cash = 0.0

    def deposit_cash(self, amount):
        if amount > 0:
            self.cash = amount + self.cash

    def withdraw_cash(self, amount):
        if amount > 0:
            amount = min(self.cash, amount)
            self.cash = self.cash - amount
            return self.cash, amount
        else:
            raise ValueError('Incorrect amount')

    def print_info(self):
        return self.number, self.cash

new_acc = BankAccount(1)
new_acc.deposit_cash(200)
print(new_acc.withdraw_cash(150))
new_acc = BankAccount(10)
print(new_acc.withdraw_cash(150))
new_acc.deposit_cash(500)
print(new_acc.withdraw_cash(200))
#new_acc = BankAccount(1)
#print(new_acc.withdraw_cash(20))
print(new_acc.print_info())