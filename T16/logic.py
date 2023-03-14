#  Ask the user to enter a number
user_num = int(input("Please, enter a positive integer: "))

# Use while loop to prints out all the even numbers from 1 up to (and possibly including) the number given by the user.
a = 0
while a < user_num:
    a += 2
    print(a)

# When the number is odd, and the code is on the last loop, the code still adds 2 to the variable a and prints the value before it breaks out of the loop.