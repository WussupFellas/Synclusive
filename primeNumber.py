def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True

def get_user_input():
    while True:
        try:
            user_input = int(input("Please enter a number to check if it is a prime number: "))
            return user_input
        except ValueError:
            print("That's not a valid number. Please try again!")

def main():
    x = get_user_input()
    if is_prime(x):
        print(f"{x} is a prime number.")
    else:
        print(f"{x} is not a prime number.")

if __name__ == "__main__":
    main()
