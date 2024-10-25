from manager import Manager
from customer import Customer
from database import Database as db

import datetime

class Bank:
    def __init__(self) -> None:
        self.admin = Manager()
        self.customers = db.read()
            
    def customer(self,name):
        self.customers = db.read()
        for cust in self.customers:
            if cust.match(name):
                return cust
        return None
    
    def add(self):
        name = input('Name: ')
        cust = self.customer(name)
        if cust != None:
            print(f'Customer already exists')
        else:
            self.customers.append(Customer(name))
            db.save(self.customers)
            
    def remove(self):
        name = input('Name: ')
        cust = self.customer(name)
        if cust != None:
            self.customers.remove(cust)
            db.save(self.customers)
        else:
            print(f'Customer does not exist')
            
    def show(self):
        name = input('Name: ')
        cust = self.customer(name)
        if cust != None:
            cust.show()
        else:
            print(f'Customer does not exist')
            
    def view(self):
        self.customers = db.read()
        for cust in self.customers:
            cust.show()
            
    def customer_login(self):
        name = input('Name: ')
        cust = self.customer(name)
        if cust != None:
            cust.menu()
            db.save(self.customers)
        else:
            print(f'Customer does not exist')            
    
    def admin_login(self,bank):
        self.admin.menu(bank)        
        
    def menu(self):
        x = datetime.datetime.now()
        print(f'Banking menu: {x.strftime("%c")}')
        choice = input(f'Browsing choices(L/A/X): ')
        
        while choice != 'X':
            match choice:
                case 'L': self.customer_login()
                case 'A': self.admin_login(self)
                case _: self.help()
            choice = input(f'Browsing choices(L/A/X): ')   
    
    def help(self):
        print("Menu options")
        print("L - Customer Login")
        print("A - Admin Login")
        print("X - exit")
        
def main():
    bank = Bank()
    bank.menu()
    
if __name__ == '__main__':
    main()