def print_lines(num_lines):
    """
    Prints the specified number of lines, each with its line number.
    
    Parameters:
    num_lines (int): The number of lines to print.
    """
    for i in range(1, num_lines + 1):
        print(f"Line #{i}")

# Ask the user for input
num_lines = int(input("Enter the number of lines you want to see: "))

# Call the function with the user's input
print_lines(num_lines)
