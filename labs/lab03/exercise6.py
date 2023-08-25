class Car:
    def __init__(self,make,pos):
        self.make = make
        self.pos = pos
        
    def move(self,distance):
        self.pos += distance
        
    def __str__(self) -> str:
        return f'{self.make} is at position {self.pos}'
    
car = Car("BMW",0)
print(car)
car.move(15)
print(car)