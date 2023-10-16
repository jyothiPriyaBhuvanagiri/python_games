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
