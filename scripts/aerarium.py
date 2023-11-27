import argparse
from aerarium.accounts import Accounts
from aerarium.utils import CONFIG_FILE_PATH, generate_config, make_config
import yaml

def load_config():
    try:
        with open(CONFIG_FILE_PATH, 'r') as file:
            config = yaml.load(file, Loader=yaml.FullLoader)
    except FileNotFoundError:
        config = generate_config()
        make_config(config)
    return config

def main():
    parser = argparse.ArgumentParser(description="Aerarium CLI Tool")
    parser.add_argument('--balance', action='store_true', help='Check account balance')
    parser.add_argument('--withdraw', type=float, help='Withdraw amount from the account')
    parser.add_argument('--deposit', type=float, help='Deposit amount into the account')

    args = parser.parse_args()

    config = load_config()
    account_name = config['account_name']
    account_balance = config['account_balance']

    a = Accounts(account_name, account_balance)

    if args.balance:
        print(f"Current balance: {a.check_balance()}")
    elif args.withdraw:
        description = input("Enter withdrawal description: ")
        category = input("Enter withdrawal category: ")
        amount = args.withdraw
        print(f"Balance: {a.withdraw(amount, description, category)}")
    elif args.deposit:
        description = input("Enter deposit description: ")
        category = input("Enter deposit category: ")
        amount = args.deposit
        print(f"Balance: {a.deposit(amount, description, category)}")
    else:
        print("No valid command provided. Use --help for usage information.")

if __name__ == '__main__':
    main()
