# ---- Task 1 - Part 1 ----#
import os

# Define the mathematical operations
# Addition func
def addition(num1, num2):
    result = num1 + num2
    print(f'{num1} + {num2} = {result}')
    return result


# Subtraction
def subtraction(num1, num2):
    result = num1 - num2
    print(f'{num1} - {num2} = {result}')
    return result


# Multiplication
def multiplication(num1, num2):
    result = num1 * num2
    print(f'{num1} x {num2} = {result}')
    return result


# Division
def division(num1, num2):
    try:
        result = num1 / num2
        print(f'{num1} / {num2} = {result}')
        return result
    except ZeroDivisionError:
        print("You cannot divide by zero!")
        return None

# Main program to calculate operations
while True:
    choice = input("Enter 'c' for calculator or 'r' to read equations from a file or 'e' to exit: ")
    if choice == 'c':
        try:
            num_1 = int(input("Enter a first number: "))
            num_2 = int(input("Enter a second number: "))
            operation = input('''Use the characters below to perform an operation:
            + for addition
            - for subtraction
            * for multiplication
            / for division\n''').lower()
            if operation == '+':
                result = num_1 + num_2
            elif operation == '-':
                result = num_1 - num_2
            elif operation == '*':
                result = num_1 * num_2
            elif operation == '/':
                result = num_1 / num_2
            else:
                print("You've chosen a wrong operation, please try again.")
                continue
            with open('equations.txt', 'a+') as f:
                equations_f = f.write(f"{num_1} {operation} {num_2} = {result}\n")
            continue
        except Exception:   # Error prevention in case user inserts characters that are not numbers
            print("Ops, please enter a number, not a string.")
    elif choice == 'r':
        equations = input("Enter the name of the file containing equations: ")
        try:
            if not os.path.isfile('equations.txt'):  # Checking if the file exists to open it for reading
                print("File doesn't exist. Use the calculator first.")
            elif equations == 'equations.txt':  # Matching the input with file's name
                with open('equations.txt', "r") as equations_r:
                    content = equations_r.read()
                    print(content)
            else:
                print("Wrong name. Try again.")
        except Exception:
            print("Ops, the name of the file is incorrect. Try again")
        continue
    elif choice == 'e':
        print("Goodbye")
        break
    else:
        print("Invalid choice, please try again.")

close_f = close()