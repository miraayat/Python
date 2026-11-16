#Python Object-Oriented-Programming

class Employee:

    raise_amount  = 1.04
    num_of_emp = 0

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + '.' + last + '@gmail.com'

        Employee.num_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Mir', 'Aayat', 60000)

Employee.set_raise_amount(1.06)
print(Employee.raise_amount)

import datetime as dt
my_date = dt.date(2004, 4, 17)
print(my_date)
print(Employee.is_workday(my_date))
# print(emp_1.salary)
# emp_1.apply_raise()
# print(emp_1.salary)
# # print(Employee.__dict__)
# print(emp_1.__dict__)

# print(emp_1)
# print(emp_2)
#--------Creating instance variables manually----------
# emp_1.name = 'Aayat'
# emp_1.email = 'miraayat504@gmail.com'
# emp_3 = Employee('Mir', 'Ayesha', '7000000')


# print(emp_1.email)
# print(emp_2.email)

# #print('{} {}'.format(emp_1.first, emp_1.last))

# print(emp_2.fullname())
# print(Employee.fullname(emp_1))

# print(Employee.num_of_emp)
