import random
x = int(input("Welcome to Rock, Papers, Scissors!\nSelect your hand:\n1 - Rock\n2 - Paper\n3 - Scissors\n"))

y = random.randint(1,3)
#randomizes a number between 1 and 3, included.

if(y == 1):
    print("The computer has selected Rock!")
elif(y == 2):
    print("The computer has selected Paper!")
else:
    print("The computer has selected Scissors!")
#Prints the selection of the CPU.

if (x == y):
    print("It's a draw!")
elif(x == 1 and y == 3) or (x == 2 and y == 1) or (x == 3  and y == 2):
    print("You win!")
else:
    print("You lose!")
#Prints if you lost or you won.