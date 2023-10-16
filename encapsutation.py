# praticing oops concepts with basic examples

class BankAccount:

    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
            return f"deposited {amount}, new_balance {self.__balance}"
        else:
            return f'deposit amount must be positive'

    def withdraw(self, amount):
        if amount > 0 <= self.__balance:
            self.__balance -= amount
            return f"withdrawn {amount}, remaining_balance {self.__balance}"

        else:
            return f'withdrawn is not possible'

    def check_the_balance(self):

        return f'current balance :{self.__balance}'


account = BankAccount(2000)
print(account.check_the_balance())

print(account.deposit(500))
print(account.withdraw(300))


#############################################################

class Person:

    def __init__(self, name):
        self.__name = name

    def set(self, name):
        if isinstance(name, str):
            self.__name = name

        else:
            return f'name is not defined'

    def get(self, name):
        return self.__name


person = Person("jjoe")

print(person.get("hjt"))
print(person.set("mad"))

