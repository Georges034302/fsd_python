import math as m

x = 4
y = 2

print(f'x + y = {x+y:07.3f}')
print(f'x - y = {x-y:07.3f}')
print(f'x / y = {x/y:07.3f}')
print(f'x * y = {x*y:07.3f}')
print(f'x % y + x / y = {x%y+x/y:07.3f}')
print(f'result = {(pow(y,7)/m.sqrt(5)+x)*(pow(x,4)%5 +2):07.3f}')
