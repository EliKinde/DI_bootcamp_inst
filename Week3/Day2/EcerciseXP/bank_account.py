class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit():
        pass

    def withdraw():
        pass

class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("The deposit amount must be a positive integer.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("The withdrawal amount must be a positive integer.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for this withdrawal.")
        self.balance -= amount

    def get_balance(self):
        return self.balance

# Example usage:
account = BankAccount()
account.deposit(100)  # Deposit 100
print(account.get_balance())  # Outputs: 100

account.withdraw(30)  # Withdraw 30
print(account.get_balance())  # Outputs: 70

try:
    account.withdraw(100)  # Attempt to withdraw more than the current balance
except ValueError as e:
    print(e)  # Outputs: Insufficient funds for this withdrawal.

try:
    account.deposit(-50)  # Attempt to deposit a negative amount
except ValueError as e:
    print(e)  # Outputs: The deposit amount must be a positive integer.

try:
    account.withdraw(-10)  # Attempt to withdraw a negative amount
except ValueError as e:
    print(e)  # Outputs: The withdrawal amount must be a positive integer.

