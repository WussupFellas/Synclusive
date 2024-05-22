x = int(input("Enter a first value: "))
y = int(input("Enter a second value: "))

result = x + y

if(result > 100):
    print("The sum of both values is higher than 100!")
elif(result < 100):
    print("The sum of both values is lesser than 100!")
else:
    print("The sum of both values equals 100!")