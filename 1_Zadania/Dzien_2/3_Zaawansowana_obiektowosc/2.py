class BankAccount:
    number = 0
    cash = 0.0
    __next_acc_number = 1
    def __init__(self):
        self.__next_acc_number = BankAccount.__next_acc_number
        self.cash = 0.0
        BankAccount.__next_acc_number += 1

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
        print(self.__next_acc_number, self.cash)



acc1 = BankAccount()
acc1.deposit_cash(500)
acc2 = BankAccount()
acc3 = BankAccount()
acc2.deposit_cash(400)
acc3.deposit_cash(200)
acc1.withdraw_cash(200)
acc1.print_info()
acc2.print_info()
acc3.print_info()