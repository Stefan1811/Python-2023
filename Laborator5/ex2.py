class Account:

    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no
    
    def deposit(self,value):
        self.balance+=value
    
    def withdrawal(self,value):
        if self.balance>=value:
            self.balance-=value
        else:
            print("Operation failed")
    
    def interest_calculation(self):
        pass

class SavingsAccount(Account):
    def interest_calculation(self):
        return self.balance*0.05

class CheckingAccount(Account):
    def interest_calculation(self):
        return self.account_no,self.balance

costumer1=SavingsAccount(3000,"RO12BTLR343CRT567")
costumer1.deposit(200)
costumer1.withdrawal(1000)
print(costumer1.balance)
print(costumer1.interest_calculation())

costumer2=CheckingAccount(2000,"RO25BTLR3990998")
costumer2.deposit(600)
costumer2.withdrawal(2000)
print(costumer2.balance)
print(costumer2.interest_calculation())


