# Ask user to enter an integer
user_num = int(input("Please, enter a positive integer: "))

# Use if statement to determine if the input follow some conditions
if user_num % 2 == 0 and user_num % 5 == 0:
    print(f"The number {user_num} is divisible by 2 and 5.")
elif user_num % 2 == 0 or user_num % 5 == 0:
    print(f"The number {user_num} is divisible by 2 or 5.")
elif user_num % 2 != 0 or user_num % 5 != 0:
    print(f"The number {user_num} is not divisible by 2 or 5.")
else:
    print("Invalid entry")