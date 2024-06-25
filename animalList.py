num_animals = int(input("How many animals in this list: "))

animal_list = []

while len(animal_list) < num_animals:
    animal_name = input("Enter an animal name:")

    if animal_name in animal_list:
        print("This animal is already in this list. Please enter a different name.")
    else:
        animal_list.append(animal_name)
        print(f"{animal_name} has been added to the list!")

print(f"The animal list is: {animal_list}")