# bank_account.py

class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: ${amount:.1f}")
            return True
        else:
            print("Deposit amount must be positive.")
            return False

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew: ${amount:.1f}")
            return True
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")
            return False

def main():
    account = BankAccount(100.0)  # Starting with a balance of $100
    account.withdraw(50.0)  # This will withdraw $50 from the account

if __name__ == "__main__":
    main()

    def display_balance(self):
        print(f"Current Balance: ${self._balance:.2f}")


# main-0.py

import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()


