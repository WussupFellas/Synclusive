numbers = int(input("How many numbers are there: "))

full_list = []

for _ in range(numbers):
    number = int(input("Enter a note: "))
    full_list.append(number)

total_sum = 0

for number in full_list:
    total_sum += number

print(f"The sum of your list is: {total_sum}")