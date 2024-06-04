def print_rectangle():

# Print the top border of the rectangle
    print('-' * w)

    # Print the middle part of the rectangle
    for _ in range(h - 2):
        print('|' + ' ' * (w - 2) + '|')

    # Print the bottom border of the rectangle
    if h > 1:
        print('-' * w)

# Ask the user for input
h = int(input("Enter the height of the rectangle: "))
w = int(input("Enter the width of the rectangle: "))

# Call the function with the user's input
print_rectangle()
