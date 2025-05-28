# multiplication table

# define the variable 

number = int(input("Enter a number to see its multiplication table:")) # prompt the user for a number

# print the multiplication table using a for loop
for y in range(1, 11):
    z = number * y
    print(f"{number} * {y} = {z}")