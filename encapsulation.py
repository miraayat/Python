class Wallet:

    def __validate(self, amount):  #private method
        if amount <= 0:
            raise ValueError('Positive no required')
        
    def __init__(self, balance):
        # self._balance = balance      #python does not enforce it(protected properties)
        self.__balance = balance #private property

    def deposit(self, amt):
        self.__validate(amt)
        self.__balance += amt

    def withdraw(self, amt):
        if self.__balance >= amt:
            self.__balance -= amt
        else:
            raise ValueError('Insufficient Funds')

    def get_balance(self):
        return self.__balance

wal = Wallet(500)
wal.deposit(100)
wal.withdraw(50)
# print(wal.__balance)  throws error

print(wal.get_balance())
wal.__balance = 1000 # creates a new __balance obj will not throw error

wal.withdraw(600)