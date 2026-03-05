try:
    # Take input from user
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Check division by zero
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        # Calculate results
        sum_result = num1 + num2
        division_result = num1 / num2

        # Print results
        print("Sum:", sum_result)
        print("Division:", division_result)

# Handle invalid input
except ValueError:
    print("Invalid input")