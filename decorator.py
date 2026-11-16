class Employee:

    raise_amount  = 1.04
    num_of_emp = 0

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

        Employee.num_of_emp += 1

    @property   #getter
    def email(self):
            return '{}.{}@gmail.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
         first, last = name.split(' ')
         self.first = first
         self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete name")
        self.first = None
        self.last = None

emp_1 = Employee('Mir', 'Aayat', 60000)

emp_1.fullname = 'Mir Ayesha'

print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname