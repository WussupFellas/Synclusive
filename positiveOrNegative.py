x = int(input("Enter a value between -10 and 10: "))

if(x > 0 and x <= 10):
    print("The value you have entered is positive.")
elif(x < 0 and x >= -10):
    print("The value you have entered is negative.")
elif(x == 0):
    print("The value you have entered is zero.")
else:
    print("The value you have entered does not meet the specified values. Please try again.")