# Open the external file DOB.txt to read
f = open('./DOB.txt', 'r')

# Create variables to hold loop results
name_string = ''
birth_string = ''

# Loop in each line and split the list 
for line in f:
    name_list = line.split(" ", 2) # Knowing that the names follow same structure with one empty space between them, split it into a list with 2 items
    name_string = name_string + "\n" + " ". join(name_list[:2]) 
    birth_string = birth_string + str(name_list[2]) # Use the remainder item as birthdate and concate all results of the loop


# Print out the names and birthdates
print(f"Name{name_string}")
print()
print(f"Birthdate\n{birth_string}")

# Close externa file
f.close()
