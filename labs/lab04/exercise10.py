n = int(input('n = '))

F0 = 1
F1 = 1

for i in range(2, n):
    Fi = F0 + F1
    print(f'F1({F0}) - F2({F1}) --> Fi = {Fi}')
    F0 = F1
    F1 = Fi

