# Set variable to hold the number of loops iterations
num_students = int(input("How many students are registered in your class?: "))

# Create a new file assigning it to a variable
f = open ('reg_form.txt', 'w+')

# Set empty variable to hold the loop outcomes
id_numbers = " "
for i in range(num_students):
    id_numbers = id_numbers + "\n" + input("Enter your ID number: ") + " " + "............................." + "\n"

# Save the loop results into the new file using the write method
f.write(f"Sign the attendance list on the right side of your ID number: \n {id_numbers} \nThanks")

f.close()