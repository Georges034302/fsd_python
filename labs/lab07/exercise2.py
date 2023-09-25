class Wallet:
    def stacked(self,value):
        notes = []
        for e in range(0,10):
            notes.append(value)
        return notes
    
    def __init__(self):
        self.price = 0
        self.coins = 0
        self.fives = self.stacked(5)
        self.tens = self.stacked(10)
        self.twenties = self.stacked(20)
        self.fifties = self.stacked(50)
        self.hundreds = self.stacked(100)
        
    def pay(self):
        price = int(input("Price $"))
        self.price = price
        while price >= 5:
            if price >= 100:               
                self.hundreds.pop()
                price -= 100
            elif price >= 50:
                self.fifties.pop()
                price -= 50
            elif price >= 20:
                self.twenties.pop()
                price -= 20
            elif price >= 10:
                self.tens.pop()
                price -= 10
            else:
                price -= 5
                self.fives.pop()
        self.coins = price
   
    def used(self,*args):
        return 10 - len(*args)   
        
    def notes(self,*args):
        return f'- uses {self.used(*args)}' if self.used(*args) >= 0 else ''
        
    def show(self):
        self.pay()
        print(f'Wallet:\n{self.notes(self.hundreds)} notes of 100\n{self.notes(self.fifties)} notes of 50\n{self.notes(self.twenties)} notes of 20\n{self.notes(self.tens)} notes of 10\n{self.notes(self.fives)} notes of 5\n- used {self.coins} coins\n')
       
def main():
    Wallet().show()
    
if __name__ == '__main__':
    main()
                
            
        
    
        