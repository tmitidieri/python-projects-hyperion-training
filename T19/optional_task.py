# Open external file DOB to read and to use as base to the new file input.txt
old_database_f = open('./DOB.txt', 'r')
old_database = old_database_f.readlines()
old_database_f.close()

# Create new file input.txt, using the DOB.txt as content to copy
new_database_f = open('./input.txt', 'w')
new_database_f.writelines(old_database)
new_database_f.close()

# Read the new file input.txt
f = open('input.txt', 'r')

# Create new variables to host the results from the for loops below
lines_total = 0
chars_total = 0
words_total = 0

# Loop lines in the file and iterate the lines total accordinlly
for line in f:
    lines_total += 1
    chars_per_line = 0  # On each iteration, reset to 0 the characteres and words to start a new counting every line 
    words_per_line = 0

# Loop characteres and words in the file and iterate the variables accordinlly
    for characters in line:
        chars_per_line += 1
        chars_total += 1

    for words in line.split(' '):
        words_per_line += 1
        words_total += 1

    # Print out the number of the lines, quantity of characters and words
    print(f"Line {lines_total}: contains {chars_per_line} characters and {words_per_line} words")

# Print out the total number of lines, characters and words in the file
print()
print(f"The file has {words_total} words, {chars_total} chars and {lines_total} lines in total")

f.close()