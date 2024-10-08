```
import sys

class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: ${amount:.2f}. New balance: ${self.account_balance:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew: ${amount:.2f}. New balance: ${self.account_balance:.2f}.")
            return True
        else:
            print("Insufficient funds or invalid amount.")
            return False

    def display_balance(self):
        print(f"Current balance: ${self.account_balance:.2f}")

if __name__ == "__main__":
    account = BankAccount()

    if len(sys.argv) != 2:
        print("Usage: python main-0.py [command:amount|display]")
        sys.exit(1)

    command = sys.argv[1]

    if command.startswith("deposit:"):
        try:
            amount = float(command.split(":")[1])
            account.deposit(amount)
        except ValueError:
            print("Invalid amount.")
    elif command.startswith("withdraw:"):
        try:
            amount = float(command.split(":")[1])
            account.withdraw(amount)
        except ValueError:
            print("Invalid amount.")
    elif command == "display":
        account.display_balance()
    else:
        print("Unknown command.")
```

### Explanation:
- This script defines a `BankAccount` class with methods for depositing, withdrawing, and displaying the balance.
- The command line interface is integrated into the `if __name__ == "__main__":` block, allowing users to interact with the account via command line arguments.
- The script checks for valid commands and handles amounts accordingly.

### Command Line Usage:
- To deposit $50: 
  ```
  python main-0.py deposit:50
  ```
- To withdraw $20 (if sufficient funds are available):
  ```
  python main-0.py withdraw:20
  ```
- To display the current balance:
  ```
  python main-0.py display
  ```
