#This is a guess the number game

import random

print('hello. What is your name?')
name = str(input())

print('Well, '+ name + ', I am thinking of a number between one and twenty.')
secretNumber = random.randint(1, 20)

for  guessesTaken in range(1,7):
    print('Take a guess')
    guess=int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break
print('You guessed '+str(guessesTaken)+' times')