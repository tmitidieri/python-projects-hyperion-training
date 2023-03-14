# creates function that print all days of the week
def week_days():
    print("Monday, Tuesday, Wednesday, Thrusday, Friday, Saturday, Sunday")


# creates a function that takes a sentence and change every second word of it to 'hello'
def change_second_word():
    sentence = input("Please, insert a sentence and see what happens: ")

    sentence = sentence.split(' ')

    for idx, word in enumerate(sentence, 1):
        if idx % 2 == 0:
            sentence[idx - 1] = 'hello'

    print(' '.join(sentence))

# calls functions
week_days()
change_second_word()