# Declare three variables called num1, num2 and num3. Assign each variable a number
num1 = 33
num2 = 33
num3 = 6

# Compare num1 and num2 and display the larger value
if num1 <= num2:
    print(f"The number {num2} is the largest value entered")
else:
    print(f"The number {num1} is the largest value entered")

# Determine whether num1 is odd or even and display the result
if num1 %2 == 0:
    print(f"The first number entered is {num1} and it is an even value.")
else:
    print(f"The first number entered is {num1} and it is an odd value.")

# Define a function to sort in ascending order the variables num1, num2, num3
def sort_list():
    num_list = (num1, num2, num3)
    print(f"The ascending order of the numbers entered is: {sorted(num_list)}")

# Write a conditional statement to sort the three numbers from largest to smallest
if num1 != num2 and num1 != num3:
    sort_list()
elif num1 == num2 and num1 ==3:
    sort_list()
elif num1 == num2 or num1 == num3:
    sort_list()
else:
    print("The end!")
