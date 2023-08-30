import random as ran 

n = int(input('n = '))

total = 0
for i in range(1,n+1):
    value = ran.randint(0,10)
    if value % 2 == 0:
        total += value
print(f'Total = {total}')
    
