# main-0.py

import sys
from bank_account import BankAccount

def main():
    account = BankAccount()

    if len(sys.argv) < 2:
        print("Usage: python main-0.py [deposit|withdraw|balance] [amount]")
        return

    action = sys.argv[1].lower()

    if action == "deposit":
        if len(sys.argv) != 3:
            print("Usage: python main-0.py deposit <amount>")
            return
        amount = float(sys.argv[2])
        account.deposit(amount)

    elif action == "withdraw":
        if len(sys.argv) != 3:
            print("Usage: python main-0.py withdraw <amount>")
            return
        amount = float(sys.argv[2])
        account.withdraw(amount)

    elif action == "balance":
        account.display_balance()

    else:
        print("Invalid action. Use deposit, withdraw, or balance.")

if __name__ == "__main__":
    main()