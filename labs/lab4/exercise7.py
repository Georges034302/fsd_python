c = input("Character: ")
count = 0

while c != ".":
    count += "aeiou".count(c.lower())
    c = input("Character: ")
    
print(f'Vowel count = {count}')
        