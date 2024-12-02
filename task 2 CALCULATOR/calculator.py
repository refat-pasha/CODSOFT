def calculator():
    print("Welcome to the calculator!")
    print("Choose an arithmetic operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")


    try:
        num1 = float(input("Enter the first number: \n"))
        num2 = float(input("Enter the second number: \n"))
        operation = input("Enter the operation (+, -, *, /): \n")


        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero is not allowed!")
                return
        else:
            print("Invalid operation! Please choose from +, -, *, /.")
            return

        # Display the result
        print()
        print(f"The result of {num1} {operation} {num2} is: {result}\n")

    except ValueError:
        print("Error: Please enter valid numbers.")


calculator()
