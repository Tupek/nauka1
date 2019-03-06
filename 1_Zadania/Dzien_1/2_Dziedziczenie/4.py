class Employee:

    id = 0
    first_name = None
    last_name = None
    salary = 0

    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def set_salary(self, salary):
        try:
            salary = float(salary)
            if salary >= 0.0:
                self.salary += salary
            else:
                raise("Warotść ujemna")
        except ValueError:
            raise ("Niepoprawna wartość")

    def info(self):
        return self.id, self.first_name, self.last_name, self.salary

class HourlyEmployee(Employee):
    hours = 0

    def compute_payment(self, hours):
        self.hours = hours
        return self.salary * hours

class SalariedEmployee(Employee):

    def compute_payment(self):
        return self.salary * 190

#e = Employee(1, "Kamil", "Nowak")
#e.set_salary(55)
#print(e.__salary)
#print(e.info())
#print(e.compute_payment(5))

#h = HourlyEmployee(1, "Kamil", "Nowak")
#h.set_salary(55)
#print(h.info())
#print(h.compute_payment(5))

s = SalariedEmployee(1, "Kamil", "Nowak")
s.set_salary(55)
print(s.compute_payment())