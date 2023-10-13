class Account:
    def __init__(self,type) -> None:
        self.type = type
        self.balance = float(input(f'{self.type} balance $'))
        
    def deposit(self,amount):
        self.balance += amount 
        
    def withdraw(self,amount):
        self.balance -= amount
        
    def transfer(self,amount,other):
        self.balance -= amount
        other.balance += amount 
        
    def __str__(self) -> str:
        return f'{self.type} balance ${self.balance:.2f}'