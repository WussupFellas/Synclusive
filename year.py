x = int(input("Enter your age: "))
y = int(input("Enter the current year: "))

z = int(y - x)
#Calculates the year the person was born in.

w = int(y - (x - 18))
#Calculates when the person made/will make 18 years old.

print("You were born in " + str(z) + ".")

if(w > y):
    print("You will be 18 years old in " + str(w) + ".")
#If the value is higher than the current year, user is not 18 yet. Will print when user will be 18.
elif(x < y):
    print("Your 18th birthday was in " + str(w) + "." )
#If the value is lower than the current year, user is already 18. Will print when user turned 18.
else:
    print("Your birtday was this year, in " + str(w) + ".")
#If the value equals the current year, user truned 18 this year.