# Ask user to input their full name and assign it to a variable
full_name = input("Please, insert your full name: ")

# Create a variable to hold the state if the data passed our validations inside the while loop
# Validate the input with if statement and define feedback messages for each condition
# Return a thank you message if the user inserts the data in the right format
passed = False
while(not passed):

    if len(full_name) == 0:
        full_name = input("You haven't entered anything, please insert your full name: ")

    elif len(full_name) < 4:
        full_name = input("You've entered less than 4 characteres. Please, make sure that you have entered your name and surname: ")

    elif len(full_name) > 25:
        full_name = input("You've entered more than 25 characteres. Please, make sure that you have only entered your full name: ")

    elif  " " not in full_name:
        full_name = input("Please, make sure that you have entered your name and surname: ")

    else:
        print(f"Thank you for entering your name, {full_name}")
        passed = True
        break