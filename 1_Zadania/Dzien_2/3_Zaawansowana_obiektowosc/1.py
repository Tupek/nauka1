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

class AdvancedCalculator(Calculator):
    PI = 3.14159265

    @staticmethod
    def compute_circle_radius(r):
        return r ** 2 * AdvancedCalculator.PI

a = AdvancedCalculator()
print(a.compute_circle_radius(5))
a.add(1, 2)
print(a.print_operations())
a.multiply(5, 5)
print(a.print_operations())
