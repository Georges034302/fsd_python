import datetime

class Manager:
    def __init__(self) -> None:
        self.name = 'John Smith'
      
    def add(self,bank):
        bank.add()
        
    def remove(self,bank):
        bank.remove()
    
    def show(self,bank):
        bank.show()
        
    def view(self,bank):
        bank.view()
    
    def menu(self,bank):
        x = datetime.datetime.now()
        print(f'{self.name} admin menu: {x.strftime("%c")}')
        choice = input(f'{self.name} choices(a/r/s/v/x): ')
        
        while choice != 'x':
            match choice:
                case 'a': self.add(bank)
                case 'r': self.remove(bank)
                case 's': self.show(bank)
                case 'v': self.view(bank)
                case _: self.help()
            choice = input(f'{self.name} choices(a/r/s/v/x): ')   
    
    def help(self):
        print("Menu options")
        print("a - add")
        print("r - remove")
        print("s - show")
        print("v - view")
        print("x - exit")
        
    