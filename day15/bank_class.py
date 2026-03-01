class Bank:
    def __init__(self,name,balance,account_no,is_active):
        self.name=name
        self.balance=balance
        self.account_no=account_no
        self.is_active=is_active

    def show_balance(self):
        print(self.balance)

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
        else:
            print("Error. Can't deposit negative amount!")

    def withdraw(self,amount):
        if amount>0 and self.balance>=amount:
            self.balance-=amount
        else:
            print("Failed. try looking at your input")

user_1 = Bank("Dagaga Addisu",1500,10005,True)
user_1.deposit(1000)
user_1.show_balance()
user_1.withdraw(300)
