class Bank:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount > 0:
            self.__balance= amount
        else:
            print("Invalid Amount")

b1 = Bank(5000)
b1.set_balance(9000)
print(b1.get_balance())

