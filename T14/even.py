#  Ask the user to enter a number
user_num = int(input("Please, enter a positive integer: "))

# Use while loop to prints out all the even numbers from 1 up to (and possibly including) the number given by the user.

a = 0
while a < user_num:
    a += 2
    if a > user_num:
        break
    print(a)
