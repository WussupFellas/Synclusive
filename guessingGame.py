import random
x = int(input("Welcome to our Guessing Game!\nWe have randomly generated a number between 1-20.\nTry guessing it: "))
y = random.randint(1,20)

while(x != y):
    if(x > y):
        x = int(input("The number you have entered is too high! Try again: "))
    elif(x < y):
        x = int(input("The number you have entered is too low! Try again: "))
    else:
        x = int(input("You have entered an incorrect value! Please try again: "))
print("You guessed it! The value is", y,"!")