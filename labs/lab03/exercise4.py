import math as m 

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))
distance = m.sqrt(pow(x1-y1,2) + pow(x2-y2,2))
print(f'The distance between A({x1},{y1}) and B({x2},{y2}) is: {distance:.3f}')