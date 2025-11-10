# Create an account
# create user account and define whether its employee, customer, 

accounts = {}

# Autogenerate account number
def get_next_account_number():
    """Generate the next available account number"""
    if not accounts:
        return "1001"
    # Get all account numbers, convert to int, find max, add 1
    existing_nums = [int(acc) for acc in accounts.keys()]
    next_num = max(existing_nums) + 1
    return str(next_num)


def create_account():
    print("\n--- Create New Account ---")

    name = input("Enter account holder name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return
    
    initial = float(input("Enter initial deposit: $"))
    if initial < 0:
        print("Initial deposit cannot be negative!")
        return
    
    pin = input("Set a 4-digit PIN: ").strip()
    if len(pin) != 4 or not pin.isdigit():
        print("PIN must be exactly 4 digits!")
        return
    
    # # Auto-generate account number
    account_number = get_next_account_number()

    accounts[account_number] = {
        "name": name,
        "balance": initial,
        "pin": pin
    }

def deposit(account_number, amount):
    if account_number in accounts:
        accounts[account_number]["balance"] += amount
        print(f"Deposited {amount}. New balance: {accounts[account_number]['balance']}")
    else:
        print("Account not found.")

def withdraw(account_number, amount):
    if account_number in accounts:
        if accounts[account_number]["balance"] >= amount:
            accounts[account_number]["balance"] -= amount
            print(f"Withdrew {amount}. New balance: {accounts[account_number]['balance']}")
        else:
            print("Insufficient funds.")
    else:
        print("Account not found.")


get_next_account_number()
create_account()


print(accounts)

