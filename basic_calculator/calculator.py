print("This calculator can be used for your basic math calculations\n")

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
print("\n")

print("Please choose the arithmetic operation you want to perform: ADD, SUBTRACT, MULTIPLY, DIVIDE")
arth_metic = input("Enter your choice: ").lower()
print("\n")

if arth_metic == "add":
    print(f"Sum: {num1} + {num2} = {num1 + num2}")
elif arth_metic == "subtract":
    print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
elif arth_metic == "multiply":
    print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
elif arth_metic == "divide":
    if num2 != 0:
        print(f"Division: {num1} / {num2} = {num1 / num2}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operation. Please choose from ADD, SUBTRACT, MULTIPLY, DIVIDE.")
