x = int(input("Enter a first value: "))
y = int(input("Enter a second value: "))
z = int(input("Enter a third value: "))
#Asks for 3 values.

if(x > y and x > z):
    print(x,"is the highest value.")
elif(y > x and y > z):
    print(y,"is the highest value.")
elif(z > y and z > x):
    print(z,"is the highest value.")
elif(x == y and x== z):
    print("The values are all the same.")
else:
    print("The value you have entered does not meet the specified values or you have entered 2 equal values. Please try again.")