class BankAccount:
    def __init__(self, acc_holder, acc_number, balance):
        self.__acc_holder = acc_holder
        self.__acc_number = acc_number
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount >0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully!")
        else:
            print("Invalid deposit amount.")
    
    def withdraw(self, amount):
        if amount <=0:
            print("Invalid withdrawal amount.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully!")
    
    def show_account(self):
        print("\n=== Bank Account Details ===")
        print(f"Account Holder: {self.__acc_holder}")
        print(f"Account Number: {self.__acc_number}")
        print(f"Current Balance: ₹{self.__balance}")

name=input("Enter Account Holder Name: ")
acc_no=input("Enter Account Number: ")
balance=float(input("Enter Opening Balance: "))

acc=BankAccount(name, acc_no, balance)

acc.show_account()

while True:
    print("\n--- MENU ---")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")   
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        amount = float(input("\nEnter amount to deposit: "))
        acc.deposit(amount)

    elif choice == '2':
        amount = float(input("\nEnter amount to withdraw: "))
        acc.withdraw(amount)
    
    elif choice == '3':
        print(f"\nCurrent Balance: ₹{acc.get_balance()}")

    elif choice == '4':
        print("\nThank you for using the bank system. Goodbye!")
        break

    else:
        print("\nInvalid choice! Please try again.")