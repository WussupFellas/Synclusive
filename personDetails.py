class Person:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality

    def year_of_birth(self, current_year):
        self.year_of_birth = current_year - self.age
        return self.year_of_birth
    
if __name__ == "__main__":

    person1 = Person("Alice", 26, "Portuguese")
    current_year = int(input("Please introduce the current year: "))
    year_of_birth = person1.year_of_birth(current_year)

print(f"My name is {person1.name}. I am {person1.nationality} and I was born in {year_of_birth}, making me {person1.age} years old.")