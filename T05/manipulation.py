
# Request user's input and save variable
str_manip = input("Please insert a sentence here: ")

# Calculate the length of the string
str_len = len(str_manip)
print(f"Lenght - {str_len}")

# Find the last letter of the string
str_last_char = str_manip[-1]
print(f"Last letter - {str_last_char}")

# Replacing every ocurrence of the last letter by @
str_manip_rep = str_manip.replace(str_last_char,"@")
print(f"Replacing - {str_manip_rep}")

# Slicing and reversing the last 3 letters of the string 
str_back = (str_manip[-3:])
print(f"Slicing and reversing - {str_back[::-1]}")

# Create new word with 5 char
beg_srt = str_manip[:3]
end_srt = str_manip[-2:]
new_srt_manip = beg_srt + end_srt
print(f"New string - {new_srt_manip}")

# Display each word on a new line
str_manip2 = str_manip.replace(" ", "\n")
print(f"Every word of the sentence in a different line - \n{str_manip2}")
