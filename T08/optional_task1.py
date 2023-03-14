# Asking user to enter an integer
num = int(input("Please, insert a positive integer: "))

# Using If statement to check if user input is odd or even number
if num % 2 == 0:
    print(f"{num} is even number")
elif num % 2 == 1:
    print(f"{num} is odd number")
print("Thanks for playing!")
