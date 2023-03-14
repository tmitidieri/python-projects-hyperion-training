# Ask user age input
birth_year = int(input("Please, enter the year you were born: "))     

# Calculating age of user
from datetime import date
current_year = date.today().year
age = int(current_year - birth_year)

# # Using if statement to print allowance message
if age >= 18:
    print("Congrats, you are old enough")
else:
    print("You are a baby and can't party")
