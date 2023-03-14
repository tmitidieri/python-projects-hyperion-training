# Ask user's weight in kilograms
user_weight = int(input("Please, enter your weight in kilograms: "))

# Ask user's height in metres
user_height = float(input("Please, enter your height in meters: "))

# Calculating user's BMI
bmi = user_weight / (user_height * user_height)


# Using if, elif and else statement, print BMI message
if bmi >= 30:
    print(f"Your BMI is {round(bmi)}, you are obese.")
elif bmi >= 25:
    print(f"Your BMI is {round(bmi)}, you are overweight.")
elif bmi >= 18.5:
    print(f"Your BMI is {round(bmi)}, your weight is normal")
elif bmi < 18.5:
    print(f"Your BMI is {round(bmi)}, you are underweight.")
else:
    print("Invalid input. Try again.")
