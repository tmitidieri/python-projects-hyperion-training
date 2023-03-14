# importing libraries
import math
import statistics

# creating an empty list to populate with user's input
users_numbers = []
print('Please, insert 10 numbers below.')

# request users input until we gather 10
# use try and except to make sure user only input a number
while len(users_numbers) < 10:
    user_input = input("New Number: ")
    try:
        user_input = float(user_input)
        users_numbers.append(user_input)
    except:
        print("Input must be an number")

# print all information based on the numbers inserted. 
print(f"The sum of all numbers is: { math.fsum(users_numbers) }")

print(f"The index of the maximum numbers is: { users_numbers.index(max(users_numbers)) }")

print(f"The index of the minimum numbers is: { users_numbers.index(min(users_numbers)) }")

print(f"The average of all numbers is: { round(math.fsum(users_numbers) / len(users_numbers), 2) }")

print(f"The median value is: { statistics.median(users_numbers) }")