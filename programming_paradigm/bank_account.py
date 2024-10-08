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

```

# Initialize the current balance
current_balance = 0

def deposit(amount):
    global current_balance
    current_balance += amount
    print(f"Deposited: ${amount}")
    print_balance()

def withdraw(amount):
    global current_balance
    if amount <= current_balance:
        current_balance -= amount
        print(f"Withdrew: ${amount}")
    else:
        print("Insufficient funds!")
    print_balance()

def print_balance():
    print(f"Current Balance: ${current_balance}")

# Example usage
if __name__ == "__main__":
    deposit(50)  # Deposit $50
    withdraw(20)  # Withdraw $20
    withdraw(40)  # Attempt to withdraw $40 (should show insufficient funds)
```

When you run this script, you should see the following output:

```
Deposited: $50
Current Balance: $50
Withdrew: $20
Current Balance: $30
Insufficient funds!
Current Balance: $30
```

To check for the correct output when attempting to withdraw more than the current balance, you can use the updated script provided earlier. 

If you run the script and attempt to withdraw an amount greater than what you have, for example:

```python
withdraw(150)  # Attempt to withdraw $150 when the balance is only $30
```

You should see the following output:

```
Insufficient funds!
Current Balance: $30
```

This output confirms that the withdrawal function is correctly identifying that there are insufficient funds for the requested withdrawal and is handling it appropriately. If you have any other scenarios you'd like to test or need further help, just let me know!

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
