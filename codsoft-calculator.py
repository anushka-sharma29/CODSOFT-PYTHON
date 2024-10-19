# Task 2 (Simple calculator program)

num1 = float(input("Enter the first digit: "))
num2 = float(input("Enter the second digit: "))
operation = input("Choose an operation (+, -, *, /): ")

# calculating
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "This is an invalid operation"

# result
print("The result is:", result)
