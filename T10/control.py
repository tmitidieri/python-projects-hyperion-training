# Ask user age input
birth_year = int(input("Please, enter the year you were born: "))     

# Calculating age of user
from datetime import date
current_year = date.today().year
age = int(current_year - birth_year)

# # Using if, elif and else statement to print allowance message
if age >= 18:
    print("You are old enough.")
elif age >= 16 and age <=18:
    print("You are almost there!")
else:
    print("You're just too young.")
