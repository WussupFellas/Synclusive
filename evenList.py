numbers = int(input("How many numbers are there: "))

full_list = []

for _ in range(numbers):
    number = int(input("Enter a note: "))
    full_list.append(number)

even_list = []
for number in full_list:
    if number % 2 == 0:
        even_list.append(number)

print(f"The list of even numbers is, {even_list}")