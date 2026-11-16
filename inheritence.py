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

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, salary, prog_lang):
        super().__init__(first, last, salary)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, salary, employees = None):
            super().__init__(first, last, salary)
            if employees == None:
                self.employees = []
            else:
                self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
            if emp in self.employees:
                self.employees.remove(emp)

    def display(self):
        for emp in self.employees:
            print('-->', emp.fullname())



# print(help(Developer))
dev_1 = Developer('mir', 'aayat', 50000, 'python')
dev_2 = Developer('sue', 'heck', 50000, 'c++')
manager = Manager('ayesha', 'mir', 80000, [dev_1])
manager.add_emp(dev_2)
# print(manager.email)

# manager.remove_emp(dev_1)

# manager.display()

print(isinstance(manager, Employee))
print(isinstance(manager, Developer))

print(issubclass(Developer, Employee))
# print(dev_1.email)
# print(dev_1.prog_lang)

# print(dev_1.salary)
# dev_1.apply_raise()
# print(dev_1.salary)