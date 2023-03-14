# Ask user to enter a number
# Print out the times table from start (1) to end (12)

num_user = int(input("Please, enter a number: "))
print(f"The time table of {num_user} is: ")

for i in range(1, 13):
    print(f"{num_user} * {i} = {num_user * i}")