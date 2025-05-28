# match case calculator

# define match case calculator variable

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ").strip()

    # Match case to perform the operation

match operation:
    case "+":
            result = num1 + num2
            print(f"The result is {result}")
    case "-":
            result = num1 - num2
            print(f"The result is {result}")
    case "*":
            result = num1 * num2
            print(f"The result is {result}")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}")
        else:
            print("Error: Division by zero is not allowed.")
            num2 = int(input("Enter the second number: "))
            if num2 != 0:
                result = num1 / num2
                print(f"The result is {result}")
            else:
                print("Error: Division by zero is still not allowed.")
    case _:
            print("Invalid operation. Please choose from +, -, *, /.")

    # End of match case calculator