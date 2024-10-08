### bank_account.py

```
class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: {amount}. New balance: {self.account_balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.account_balance}.")
            return True
        else:
            print("Insufficient funds or invalid amount.")
            return False

    def display_balance(self):
        print(f"Current balance: {self.account_balance}")


if __name__ == "__main__":
    account = BankAccount()
    account.display_balance()
```

### main-0.py

```
import sys
from bank_account import BankAccount

def main():
    account = BankAccount()

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command> <amount>")
        return

    command = sys.argv[1].lower()

    if command == "deposit":
        if len(sys.argv) != 3:
            print("Usage: python main-0.py deposit <amount>")
            return
        amount = float(sys.argv[2])
        account.deposit(amount)

    elif command == "withdraw":
        if len(sys.argv) != 3:
            print("Usage: python main-0.py withdraw <amount>")
            return
        amount = float(sys.argv[2])
        account.withdraw(amount)

    elif command == "balance":
        account.display_balance()

    else:
        print("Unknown command. Use 'deposit', 'withdraw', or 'balance'.")

if __name__ == "__main__":
    main()
```

### Explanation of the Code

1. BankAccount Class:
   - The `BankAccount` class initializes with an `account_balance`, which defaults to zero if no initial balance is provided.
   - The `deposit` method checks if the amount is positive before adding it to the balance.
   - The `withdraw` method checks if the amount is valid and if sufficient funds are available before deducting it.
   - The `display_balance` method prints the current balance.

2. Command Line Interaction:
   - The `main-0.py` script takes command line arguments to perform operations on the `BankAccount` instance.
   - It checks the command (deposit, withdraw, or balance) and performs the corresponding action.
   - It provides usage instructions if the arguments are not correct.

### Running the Code

You can run the `main-0.py` script from the command line with the following commands:
- To deposit: `python main-0.py deposit 100`
- To withdraw: `python main-0.py withdraw 50`
- To check balance: `python main-0.py balance`

This setup will help you understand the fundamentals of OOP in Python while working with the `BankAccount` class.


