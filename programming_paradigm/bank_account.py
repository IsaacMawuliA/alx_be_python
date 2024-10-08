### bank_account.py

This script will define the `BankAccount` class with the necessary methods.

```
class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew: ${amount:.2f}")
            return True
        else:
            print("Insufficient funds or invalid amount.")
            return False

    def display_balance(self):
        print(f"Current balance: ${self.account_balance:.2f}")
```

### main-0.py

This script will interface with the `BankAccount` class using command line arguments.

```python
import sys
from bank_account import BankAccount

def main():
    account = BankAccount()

    while True:
        print("\nOptions: deposit, withdraw, display, exit")
        action = input("Enter action: ").strip().lower()

        if action == "deposit":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        
        elif action == "withdraw":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        
        elif action == "display":
            account.display_balance()
        
        elif action == "exit":
            print("Exiting...")
            break
        
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()
```
