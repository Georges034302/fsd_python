import datetime
from account import Account

class Customer:
    def __init__(self,name) -> None:
        self.name = name 
        self.accounts = []
        self.initialize()
        
    def initialize(self):
        self.accounts.append(Account('Savings'))
        self.accounts.append(Account('Loan'))        
        
    def match(self,name):
        return self.name == name 
    
    def account(self,type):
        for acc in self.accounts:
            if acc.type == type:
                return acc
        return None
        
    def deposit(self):
        savings = self.account('Savings')
        if(savings != None):
            amount = float(input('Amount to deposit $'))          
            savings.deposit(amount)
        else:
            print('No such account')
            
    def withdraw(self):
        savings = self.account('Savings')
        if(savings != None):
            amount = float(input('Amount to withdraw $'))
            if savings.amount >= amount:
                savings.withdraw(amount)
            else:
                print('Insufficient funds')
        else:
            print('No such account')
            
    def transfer(self):
        savings = self.account('Savings')
        loan = self.account('Loan')
        amount = float(input('Amount to transfer $'))
        if(savings != None):            
            if savings.amount >= amount:
                if loan != None:
                    savings.trasnfer(amount,loan)
                else:
                    print('No such account')
            else:
                print('Insufficient funds')
        else:
            print('No such account')
            
    def show(self):
        x = datetime.datetime.now()
        print(f'{self.name} bank statement: {x.strftime("%c")}')
        for acc in self.accounts:
            print(acc, end=' | ')
        print()
        
    def menu(self):
        x = datetime.datetime.now()
        print(f'{self.name} customer menu: {x.strftime("%c")}')
        choice = input(f'{self.name} choices(d/w/t/s/x): ')
        
        while choice != 'x':
            match choice:
                case 'd': self.deposit()
                case 'w': self.withdraw()
                case 't': self.transfer()
                case 's': self.show()
                case _: self.help()
            choice = input(f'{self.name} choices(d/w/t/s/x): ')   
    
    def help(self):
        print("Menu options")
        print("d - deposit")
        print("w - withdraw")
        print("t - transfer")
        print("s - show")
        print("x - exit")
    