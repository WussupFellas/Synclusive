def get_values():
    try:
        x = float(input("Introduce a first value: "))
        y = float(input("Introduce a second value: "))
    except ValueError:
        print("Invalid Input. Please enter a numerical value.")
        return None, None
    return x, y

def get_operation():
    z = int(input("Select the operation type you wish to use!\n1 - Addition(+)\n2 - Subtraction(-)\n3 - Multiplication(x)\n4 - Division(/)\n"))
    return z

def calculate(x, y, z):
    if(z == 1):
        return x + y
    elif(z == 2):
        return x - y
    elif(z == 3):
        return x * y
    elif(z == 4):
        if x != 0 and y != 0:
            return x / y
        else:
            return "Error: Division by Zero is not allowed."
    else:
        return "Invalid Operation Selected."
    
def main():
    x, y = get_values()
    z = get_operation()
    result = calculate(x, y, z)
    print(f"The result is {result}")

if __name__ == "__main__":
    main()
