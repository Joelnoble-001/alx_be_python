# match case calculator

# define match case calculator variable

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

while True:
    operation_type = input("Choose the operation (+, -, *, /): ").strip()

    # Match case to perform the operation

    match operation_type:
        case "+":
            result = num1 + num2
            print(f"The result is {result}")
            break  # Exit the loop after a successful operation
        case "-":
            result = num1 - num2
            print(f"The result is {result}")
            break  # Exit the loop after a successful operation
        case "*":
            result = num1 * num2
            print(f"The result is {result}")
            break  # Exit the loop after a successful operation
        case "/":
            if num2 != 0:
                result = num1 / num2
                print(f"The result is {result}")
            else:
                print("Error: Division by zero is not allowed.")
                num2 = int(input("Enter the second number: "))
                result = num1 / num2
                print(f"The resuslt is {result}")
            break  # Exit the loop after a successful operation
        case _:
            print("Invalid operation. Choose from +, -, *, /.")

    # End of match case calculator