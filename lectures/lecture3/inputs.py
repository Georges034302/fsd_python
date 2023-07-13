import sys 

# reading input from STDIN
# name = input("Name: ")
# print(name)

# var0 = sys.argv[0]
# var1 = sys.argv[1]
# var2 = sys.argv[2]
# var3 = sys.argv[3]

# print(var0)
# print(var1)
# print(var2)
# print(var3)

x = int(input("x = "))
y = int(input("y = "))

result = x*y
print(result)
print(type(result))

x = int(sys.argv[1])
y = float(sys.argv[2])

result = x/y
print(f'{result:.3f}')
print(type(result))