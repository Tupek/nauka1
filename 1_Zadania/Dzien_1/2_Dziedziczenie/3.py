class Employee:

    id = 0
    first_name = None
    last_name = None
    __salary = 0

    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def set_salary(self, salary):
        try:
            salary = float(salary)
            if salary >= 0.0:
                self.__salary += salary
            else:
                print("Warotść ujemna")
        except ValueError:
            print ("Niepoprawna wartość")

    def info(self):
        return self.id, self.first_name, self.last_name, self.__salary

class HourlyEmployee(Employee):
    hours = 0

    def compute_payment(self, hours):
        self.hours = hours
        return __salary * hours

#e = Employee(1, "Kamil", "Nowak")
#e.set_salary(55)
#print(e.__salary)
#print(e.info())
#print(e.compute_payment(5))

h = HourlyEmployee(1, "Kamil", "Nowak")
h.set_salary(55)
print(h.info())
print(h.compute_payment(5))

# tutaj coś nie wychodzi, nie wiem dlaczego ale nie chce pobrać __salary
