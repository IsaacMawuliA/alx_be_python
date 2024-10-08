# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance  # Protected attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Deposit amount must be positive.")

is_withdrawing = False

    def withdraw(self, amount):
        global is_withdrawing
        if is_withdrawing:
           return  # Prevent multiple withdrawals

        if amount > 0 and amount <= self._balance:
            is_withdrawing = True
            self._balance -= amount
            print(f"Withdrew: ${amount:.1f}")
            is_withdrawing = False  # Reset after the transaction
           return True
        elif amount > 0:
            print("Insufficient funds.")
            return False

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


