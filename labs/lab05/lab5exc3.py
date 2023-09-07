
def readString():
    return input("String: ")

def vowelCount(sentence):
    count = 0
    for c in 'aeiou':
        count += sentence.count(c)
    return count 

def show():
    s = readString()
    while s != '*':
       print(f'Vowel count = {vowelCount(s.lower())}') 
       s = readString()
show()
    