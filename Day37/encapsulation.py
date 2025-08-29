class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.__account_holder = account_holder  # Private attribute
        self.__balance = initial_balance      # Private attribute

    def account_holder(self):
        return self.__account_holder

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

# Usage
my_account = BankAccount(account_holder="Alice", initial_balance=1000)
# my_account.balance()
print(f"Account holder: {my_account.account_holder}")
# my_account.deposit(200)
# my_account.withdraw(500)
# Attempting to directly access or modify private attributes is discouraged
# print(my_account.__balance) # This would raise an AttributeError