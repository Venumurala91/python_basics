class bankaccount:
    def __init__(self,account_number,balance,amount):
        self.account_number=account_number
        self.balance=balance
        self.amount=amount


    def deposit(self,amount):
        total_balance= self.balance+self.amount
        self.balance=total_balance
        print(self.balance)
        print(f"added money ",total_balance)


    def withdraw(self,amount):
        withdraw_amount= self.balance- self.amount
        # print(self.balance)
        if withdraw_amount <=0:
            print("balance is insufficient")
        else:
            print("withdrawll_amount:",str(withdraw_amount))


    def display_balance(self):
        print(f"current_balance",{self.balance})






class customer:
    pass

b=bankaccount("12345678910",2000,500)
print(b.deposit(500))
print(b.withdraw(250))