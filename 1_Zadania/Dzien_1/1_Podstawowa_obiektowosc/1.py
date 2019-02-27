# Kalkulator, ale to chyba nie tak miało być zrobione do poprawki

class Calc():

    @staticmethod
    def add(x, y):
        return x + y
        
    @staticmethod
    def div(x, y):
        try:
            return x / y
        except ZeroDivisionError:
            return("Nie dziel przez zero cholero!")
        
    @staticmethod
    def sub(x, y):
        return x - y
        
    @staticmethod
    def mul(x, y):
        return x * y

    @staticmethod
    def get_numbers():
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Number hasn't any value.")
            return Calc.again()

    @staticmethod
    def get_operator():
        operator = input('Please enter an operator (+, -, *, /): ')
        return operator

    @classmethod
    def again(self):
        calc_again = input('''
        Do You want calculate again?
        Please type Y for YES or N for NO.
        ''')
        if calc_again.upper() == 'Y':
            Calc.calculate()
        elif calc_again.upper() == 'N':
            print('See You later.')
        else:
            self.again()

# tu cos jest nie tak z tymi print_options
    @classmethod
    def calculate(self):
        try:
            num1, num2 = self.get_numbers()
            operator = self.get_operator()
            if operator == '+':
                result = (self.add(num1, num2))
                add = ("Added {} to {} got: {}.").format(num1, num2, result)
                print(add)
                print_operations.myList.append(add)
                Calc.again()
            elif operator == '-':
                result = (self.sub(num1, num2))
                sub = ("Subtract {} from {} got: {}.").format(num1, num2, result)
                myList.append(sub)
                print(sub)
            elif operator == '*':
                result = (self.mul(num1, num2))
                mul = ("Multiplied {} with {} got: {}.").format(num1, num2, result)
                myList.append(mul)
                print(mul)
            elif operator == '/':
                result = (self.div(num1, num2))
                div = ("Divide {} by {} got: {}.").format(num1, num2, result)
                myList.append(div)
                print(div)
            else:
                print('You have not typed a valid operator, please run the program again.')
            Calc.again()
        except Exception:
            pass

    @classmethod
    def print_operations(self):
        myList = []
        return myList

# print_operations jest chyba proste, musze dac wyniki do
# innej klasy i wtedy jak wywowam print to to wyswietli ;)

# jednak nie jest proste xd, wyświetla liste ale nie z metody

Calc.calculate()
