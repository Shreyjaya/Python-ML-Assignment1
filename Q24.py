# Q24 Write a program that acts as a simple calculator. It should take two
#numbers and an operator (+, -, *, /) as input and print the result.

num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero is not allowed.")
        exit(0)
else:
    print("Error: Invalid operator.")
    exit(0)

print("The result is", result)
