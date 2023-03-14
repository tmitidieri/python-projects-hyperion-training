# Replacing elements in a string

original_pangram = "The!quick!brown!fox!jumps!over!the!lazy!dog!."
spaced_pangram = (original_pangram.replace("!"," "))
print(spaced_pangram)

# Removing last space in the string
cleaned_pangram = (spaced_pangram.replace(" .","."))
print(cleaned_pangram)

# Manipulating elements in a string
print(cleaned_pangram.upper())