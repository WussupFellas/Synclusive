x = int(input("Introduce a first value: "))
y = int(input("Introduce a second value: "))
z = int(input("Select the operation type you wish to use!\n1 - Addition(+)\n2 - Subtraction(-)\n"))

if(z == 1):
    print(x,"+",y,"=",x + y)
elif(z == 2):
    print(x,"-",y,"=",x - y)
else:
    print("An error has occurred, please try again.")