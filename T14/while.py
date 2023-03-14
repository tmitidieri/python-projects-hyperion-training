# Ask user a number, save entries in a array
# Stop requesting numbers if user enters -1, don't save this in a variable
# Calculate the average of the numbers entered, excluding the -1


num_list = []
num = ""
while num != -1:
    num = int(input("Enter a number, from -10 to 10: "))
    if num == -1:
        break
    else:  
        num_list.append(num)

average_list = sum(num_list) / len(num_list)

print(f"The list of numbers entered is: {num_list}")
print(f"The average of numbers entered is: {average_list}")
