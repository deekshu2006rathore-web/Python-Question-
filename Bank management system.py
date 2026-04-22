import random
import json
 
#-------------------------------- 
# Class for a single bank account 
#-------------------------------- 
class Account: 
    """ 
    Represents a single bank account with basic functionalities like 
    deposit, withdraw, and balance check. 
    """ 
    def _init_(self, name, initial_deposit): 
        self.name = name 
        self.balance = initial_deposit 
        self.account_number = self.generate_account_number() 
        print(f"Account for '{self.name}' created successfully.") 
        print(f"Your Account Number is: {self.account_number}") 
 
    def generate_account_number(self): 
        """Generates a random 10-digit account number.""" 
        return ''.join([str(random.randint(0, 9)) for _ in range(10)]) 
 
    def deposit(self, amount): 
        """Deposits a specified amount into the account.""" 
        if amount > 0: 
            self.balance += amount 
            print(f"Successfully deposited ${amount:.2f}. New balance: ${self.balance:.2f}") 
        else: 
            print("Invalid deposit amount. Please enter a positive number.") 
 
    def withdraw(self, amount): 
        """Withdraws a specified amount from the account if funds are sufficient.""" 
        if 0 < amount <= self.balance: 
            self.balance -= amount 
            print(f"Successfully withdrew ${amount:.2f}. New balance: ${self.balance:.2f}") 
        else: 
            print("Invalid withdrawal amount or insufficient funds.") 
 
    def check_balance(self): 
        """Prints the current balance of the account.""" 
        print(f"Current balance for account {self.account_number}: ${self.balance:.2f}") 
 
    def display_details(self): 
        """Displays the full details of the account.""" 
        print("\n--- Account Details ---") 
        print(f"Account Holder: {self.name}") 
        print(f"Account Number: {self.account_number}") 
        print(f"Balance: ${self.balance:.2f}") 
        print("-----------------------") 
 
#-------------------------------- 
# Class for managing the entire bank 
#-------------------------------- 
class Bank: 
    """ 
    Manages all bank accounts and top-level operations like creating, 
    closing, and accessing accounts. 
    """ 
    def _init_(self): 
        self.accounts = {}  # Dictionary to store account_number: Account_object 
 
    def create_account(self): 
        """Guides the user through creating a new account.""" 
        name = input("Enter account holder's name: ") 
        if not name.strip(): 
            print("Name cannot be empty.") 
            return 
             
        try: 
            initial_deposit = float(input("Enter initial deposit amount: $")) 
            if initial_deposit < 0: 
                print("Initial deposit cannot be negative.") 
                return 
            new_account = Account(name, initial_deposit) 
            self.accounts[new_account.account_number] = new_account 
        except ValueError: 
            print("Invalid input for deposit. Please enter a valid number.") 
 
    def find_account(self, account_number): 
        """Finds and returns an account object based on the account number.""" 
        return self.accounts.get(account_number) 
 
    def close_account(self): 
        """Closes an account after confirming with the user.""" 
        account_number = input("Enter the account number to close: ") 
        account = self.find_account(account_number) 
        if account: 
            confirm = input(f"Are you sure you want to close the account for {account.name}? (yes/no): ").lower() 
            if confirm == 'yes': 
                del self.accounts[account_number] 
                print("Account closed successfully.") 
            else: 
                print("Account closure cancelled.") 
        else: 
            print("Account not found.") 
 
    def perform_transaction(self): 
        """Handles transactions for an existing customer.""" 
        account_number = input("Enter your account number: ") 
        account = self.find_account(account_number) 
 
        if not account: 
            print("Account not found. Please check the account number and try again.") 
            return 
 
        print(f"\nWelcome, {account.name}!") 
        while True: 
            print("\nTransaction Menu:") 
            print("1. Deposit") 
            print("2. Withdraw") 
            print("3. Check Balance") 
            print("4. View Account Details") 
            print("5. Return to Main Menu") 
             
            try: 
                choice = int(input("Enter your choice (1-5): ")) 
 
                if choice == 1: 
                    amount = float(input("Enter amount to deposit: $")) 
                    account.deposit(amount) 
                elif choice == 2: 
                    amount = float(input("Enter amount to withdraw: $")) 
                    account.withdraw(amount) 
                elif choice == 3: 
                    account.check_balance() 
                elif choice == 4: 
                    account.display_details() 
                elif choice == 5: 
                    break 
                else: 
                    print("Invalid choice. Please enter a number between 1 and 5.") 
            except ValueError: 
                print("Invalid input. Please enter a number.") 

 
# Inside the Bank class 
def save_data(self, filename="bank_data.json"): 
    # We can't save the Account objects directly, so we create a dictionary of their data 
    data_to_save = {} 
    for acc_num, account_obj in self.accounts.items(): 
        data_to_save[acc_num] = { 
            'name': account_obj.name, 
            'balance': account_obj.balance 
        } 
     
    with open(filename, 'w') as f: 
        json.dump(data_to_save, f, indent=4) 
    print("Data saved successfully.")
 
#-------------------------------- 
# Main execution block 
#-------------------------------- 
def main(): 
    """The main function to run the bank application.""" 
    my_bank = Bank() 
 
    while True: 
        print("\n===== Welcome to Python Bank =====") 
        print("1. Create New Account") 
        print("2. Access Existing Account") 
        print("3. Close an Account") 
        print("4. Exit") 
         
        try: 
            choice = int(input("Enter your choice (1-4): ")) 
 
            if choice == 1: 
                my_bank.create_account() 
            elif choice == 2: 
                my_bank.perform_transaction() 
            elif choice == 3: 
                my_bank.close_account() 
            elif choice == 4: 
                print("Thank you for using Python Bank. Goodbye!") 
                break 
            else: 
                print("Invalid choice. Please select a valid option.") 
        except ValueError: 
            print("Invalid input. Please enter a number.") 
 
if _name_ == "_main_": 
    main()