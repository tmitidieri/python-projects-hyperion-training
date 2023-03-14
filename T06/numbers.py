# Request user input for one whole number
# Store input in a variable called A
# Request user input for one whole number
# Store input in a variable called B
# Request user input for one whole number
# Store input in a variable called C
# Calculate the SUM of A, B, C
# Calculate A minus B
# Calculate C multiplied A
# Calculate the SUM of A, B, C divided by C


a = int(input("Please, insert one positive whole number: "))
b = int(input("Please, insert one positive whole number: "))
c = int(input("Please, insert one positive whole number: "))

sum = int(a + b + c)
minus = int(a - b)
multip = int(c * a)
divis = int(sum / c)

print(f"The sum of all numbers is {sum} \nThe first number minus the second one is {minus} \nThe third number multiplied by the first number is {multip} \nThe sum of all three numbers divided by the third number is {divis}")