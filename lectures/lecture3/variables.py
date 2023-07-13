
x = 2
y = 3.5

print(type(x))
print(type(y))

x = True
y = "hello"

print("x type is "+str(type(x)))
print("y type is ",type(y))

x = 4
y = 3

y += x # y = y + x
print(y)

y /=x # y = y/x
print(y)

y -= 2
print(y)

y += x
print(y)

print(x**2)
print(pow(x,2))

print(x%3)

y = x + 3 * 4
print(y)

y= (x+3) * 4
print(y)

print(x == y)
print(x is y)

print(x != y)
print(not(x == y))
print(x is not y)

b = (not(x) and y > x) or (x+3 > 4)
print(b)