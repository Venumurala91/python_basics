class bankaccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
        # self.amount=amount


    def deposit(self,amount):
        total_balance= self.balance+amount
        self.balance=total_balance
        print(self.balance)
        print(f"added money ",total_balance)
        return ''

    def withdraw(self,amount):
        withdraw_amount= self.balance- amount
        self.balance=withdraw_amount
        # print(self.balance)
        if withdraw_amount <=0:
            print("balance is insufficient")
        else:
            print("withdrawll_amount:",amount)
            print("Remaining_balance_amount:",self.balance)

        return ''


    def display_balance(self):
        print(f"current_balance",self.balance)
        return ''

class customer:
    pass

b=bankaccount("12345678910",2000)
print(b.deposit(501))
print(b.withdraw(250))
print(b.display_balance())





