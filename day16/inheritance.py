class Bank:
    def __init__(self, name, balance, account_no, is_active):
        self.name = name
        self.balance = balance
        self.account_no = account_no
        self.is_active = is_active

    def show_balance(self):
        print(self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Error. Can't deposit negative amount!")

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
        else:
            print("You don't have anything to withdraw!")


class SavingsAccount(Bank):
    pass


class CheckingsAccount(Bank):

    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
        else:
            print("Invalid withdrawal amount.")


# Testing the classes

user_1 = SavingsAccount("Dagaga Addisu", 1500, 1000511373275, True)
user_1.deposit(1000)
user_1.show_balance()
user_1.withdraw(300)

print("-----")

user_2 = CheckingsAccount("Dagaga Addisu", 1500, 1000511373275, True)
user_2.withdraw(5000)  # overdraft allowed
user_2.show_balance()
