import math as m 

header = f'| {"i":^3s} | {"sqrt":^7s} | {"exp":^9s} |'

[print('-',end='') for c in range(1,len(header)+1)]     
print('\n'+header)
[print('-',end='') for c in range(1,len(header)+1)]  
print()
for i in range(1,11):
    print(f'| {i:^3d} | {m.sqrt(i):^7.2f} | {m.exp(i):<9.2f} |')
[print('-',end='') for c in range(1,len(header)+1)] 
print()
