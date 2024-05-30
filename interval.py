x = int(input("Introduce a value: "))
y = int(input("Introduce another value: "))

if(x > y):
    for z in range(y, x):
        z += 1
        print(z)
elif(x < y):
    for z in range(x, y):
        z += 1
        print(z)
elif( x == y):
    print("The values you have entered are equal.")
else:
    print("An error has ocurred. Please try again.")