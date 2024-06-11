# Q23 Write a program that converts temperature from Celsius to Fahrenheit
#and vice versa based on user input.
# Ask the user for input
temp_type = input("Enter 'C' to convert from Celsius to Fahrenheit or 'F' to convert from Fahrenheit to Celsius: ")
temp = float(input("Enter the temperature: "))

if temp_type.upper() == 'C':
    # Convert Celsius to Fahrenheit
    fahrenheit = temp * 9/5 + 32
    print("The temperature in Fahrenheit is ",fahrenheit)
elif temp_type.upper() == 'F':
    # Convert Fahrenheit to Celsius
    celsius = (temp - 32) * 5/9
    print("The temperature in Celsius is" ,celsius)
else:
    print("Invalid input. Please enter 'C' or 'F'.")
