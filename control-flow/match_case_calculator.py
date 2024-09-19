# Prompt the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask for the type of operation to perform
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation using Match Case
result = match operation:
    case "+":
        num1 + num2
    case "-":
        num1 - num2
    case "*":
        num1 * num2
    case "/":
        if num2 != 0:
            num1 / num2
        else:
            "Division by zero is not allowed."
    case _:
        "Invalid operation selected."

# Output the result of the operation
if isinstance(result, str):
    print(result)
else:
    print("The result is", result)
