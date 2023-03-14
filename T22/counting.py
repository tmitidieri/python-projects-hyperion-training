# Requesting input for a word
word = list(input('Type a word: '))
# Counting the number of times a character occurs in a word
letter_counting = {}
for letter in word:
    letter_counting[letter] = letter_counting.get(letter, 0)+1

print(letter_counting)
