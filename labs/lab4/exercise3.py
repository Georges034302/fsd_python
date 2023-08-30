
n = int(input('n = '))

while n != 0:
    [print('*',end='') for i in range(1,n+1)]
    print()
    n = int(input('n = '))