# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False  # Indicates deposit failed
        else:
            self.__account_balance += amount
            print(f"We deposited: ${amount:.1f}")
            return True  # Indicates deposit was successful

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False  # Indicates withdrawal failed
        elif amount > self.__account_balance:
            print("Insufficient funds.")
            return False  # Indicates withdrawal failed
        else:
            self.__account_balance -= amount
            print(f"Withdrew: ${amount:.1f}")
            return True  # Indicates withdrawal was successful

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:.2f}")

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


