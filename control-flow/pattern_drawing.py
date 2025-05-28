# pattern_drawing

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# row counter
row = 0

# Use a while loop to control the number of rows
while row < size:

    # Use a for loop to print asterisks in each row
    for column in range(size):
        print("*", end="")
    print()  # Move to a new line after each row

    row += 1
# End of pattern drawing