# Create a string and save im a variable
original_string = input("Please, insert a sentence: ")

# Use loop to extract and alternate case in the string
new_alt_char_string = ""

# Use enumerate to access the indexes and control better the item/case alternation
for index, item in enumerate(original_string):
    if index % 2 == 0:
        new_alt_char_string = new_alt_char_string + item.lower()
    else:
        new_alt_char_string = new_alt_char_string + item.upper()

print(new_alt_char_string)

# With the same string but making each alternative word lower and upper case
split_string = original_string.split(" ")
new_alt_word_string = [] # Split converts a string into an array

for index, item in enumerate(split_string):
    if index % 2 == 0:
        new_alt_word_string.append(item.lower()) # Use .append to manipulate the array
    else:
        new_alt_word_string.append(item.upper())

print(" ".join(new_alt_word_string)) # Use .join to include the empty spaces