# temperature conversion tool

# define global variables
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def  convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

#User interaction
try:
    temp_input = input("Enter the temperature to convert: ")
    temperature = float(temp_input)
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'C':
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {result}°F")

    elif unit == 'F':
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is equal to {result}°C")

    else:
        print("Invalid unit. Enter 'C' for Celsius or 'F' for Fahrenheit.")

except ValueError:
    raise ValueError("Invalid temperature. Please enter a numeric value.")