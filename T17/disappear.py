# Ask user to input a string
start_string = input("Please, insert a sentence: ")

# Ask user which characteres they want to make it disappear
disapear_list = input("Please, which characters you want to make disappear(separeted by space): ").split(" ")

# Replace the items one at a time using for loop
for item in disapear_list:
    start_string = start_string.replace(item, "")

print(f"The final string is: \n {start_string}")