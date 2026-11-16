print(1+ 2)
print('a' + 'b')

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

    def __repr__(self):
        return "Employee('{}','{}', '{}')".format(self.first, self.last, self.salary)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.salary + other.salary

    def __len__(self):
        return len(self.fullname()) - 1

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Mir', 'Aayat', 60000)
emp_2 = Employee('Filzah', 'Fida', 60000)
emp_3 = Employee('Justin', 'thv', 30000)

print(len(emp_1))

# print( emp_1 + emp_2)

# print('test'.__len__())
# print(emp_1)

# print(repr(emp_1))
# print(str(emp_1))

# print(emp_1.__repr__())

print(help(Employee))