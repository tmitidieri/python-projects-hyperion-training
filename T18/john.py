# Takes in a user’s input as a string while the string is not “John”, add every string entered to a list until “John” is entered.
# Store all incorrectly entered strings in a list where “John” is the only correct string
name = "".format()
names_list = []

while name != "John":
    name = input("Guess a name: ").capitalize()
    names_list.append(name)

names_list.remove("John")

# Converting list into a string using join
list_to_string = ', '.join(names_list)      # Join does a loop 

# Print out the list of incorrect names
print(f"The list of incorrect guesses is: {list_to_string}")
