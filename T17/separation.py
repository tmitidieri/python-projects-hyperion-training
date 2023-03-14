# Create a string and save im a variable
original_string = input("Please, insert a sentence: ")

# Displays each word of the sentence on a separate line using split and after join methods
new_word_string = original_string.split(" ")

final_string = "\n".join(new_word_string)

print(f"When we split the entered sentence in multiple lines, this is the final result: \n{final_string}")