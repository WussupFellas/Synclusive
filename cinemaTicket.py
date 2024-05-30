x = int(input("Welcome to our cinemas!\nEnter your age:\n"))

if(x >= 18):
    print("Your ticket costs 10€.")
elif(x < 18 and x >= 12):
    print("Your ticket costs 7€.")
elif(x < 12):
    print("Your ticket costs 5€.")
else:
    print("The value you have entered does not meet the specified values. Please try again.")