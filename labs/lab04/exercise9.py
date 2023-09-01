import random as ran
guess = int(input("Guess ? value = "))

correct = ran.randint(1,11)

while guess != correct:
    print('Sorry - try again')
    guess = int(input("Guess ? value = "))
    
print(f'Success, secret number = {correct}')