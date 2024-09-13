# Unlike Java, Python does not offer multiple constructors option
# Instead Python offers a work-around using class methods

class Product:
    def __init__(self,type,quantity, price):
        self.type = type
        self.price = price
        self.quantity = quantity
        
    @classmethod
    def default_constructor(cls):
        return cls(input('Type: '),int(input('Quantity: ')), float(input('Price: ')))
    
    def is_empty(self):
        self.quantity == 0
        
    def stocked(self,stock):
        self.quantity += stock
        return stock * self.price
    
    def sold(self, stock):
        self.quantity -= stock
        return stock * self.price
    
    def has(self, stock):
        return self.quantity >= stock
    
    def cash(self,stock):
        return self.price * stock
    
    def __str__(self) -> str:
        if self.quantity >= 0:
            return f'{self.type} level: {self.quantity} at price ${self.price:.2f}'
        else:
            return f'{self.type} level: {self.quantity}'
         
class CashRegister:
    def __init__(self):
        self.cash = 0.0
        
    def gain(self,amount):
        self.cash += amount
        
    def pay(self, amount):
        self.cash -= amount
        
    def isEmpty(self):
        self.cash == 0
        
    def has(self, amount):
        return self.cash >= amount
    
    def __str__(self) -> str:
        return f'Cash level ${self.cash:.2f}' if self.cash >=0 else f'Cash register is empty'
            
class Shop:
    def __init__(self):
        self.product = Product('Notebook',10,4.5)
        self.register = CashRegister()
        
    def sell(self):
        quantity = int(input("Quantity: "))
        if self.product.has(quantity):
            self.register.gain(self.product.sold(quantity))
        else:
            print('Not enough stock')
            
    def restock(self):
        quantity = int(input("Quantity: "))
        cash = self.product.cash(quantity)
        
        if self.register.has(cash):
            self.register.pay(self.product.stocked(quantity))
        else:
            print('Not enough funds!')
            
    def view(self):
        print(self.product)
        print(self.register)
        
    def menu(self):
        choice = input('Choice(s/r/v/x): ')
        
        while choice != 'x':
            match choice:
                case 's': self.sell()
                case 'r': self.restock()
                case 'v': self.view()
                case _: print('Unknown choice')
            choice = input('Choice(s/r/v/x): ')
            
def main():
    shop = Shop()
    shop.menu()
    
if __name__ == '__main__':
    main()  
        
    
        
    