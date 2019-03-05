# uważam że moja wersja byla lepsza ;P

class Calculator:

    def __init__(self):
        self.operations = []

    def add(self, num1, num2):
        r = num1 + num2
        s = 'Added {} to {} got {}'.format(num1, num2, r)
        self.operations.append(s)
        return r

    def multiply(self, num1, num2):
        r = num1 * num2
        s = 'Multiplied {} with {} got {}'.format(num1, num2, r)
        self.operations.append(s)
        return r

    def print_operations(self):
        for i in self.operations:
            print(i)

c1 = Calculator()
c1.print_operations()
c1.add(1, 2)
c1.print_operations()
c1.multiply(2, 3)
c1.print_operations()
c1.add(5, 4)
c1.print_operations()