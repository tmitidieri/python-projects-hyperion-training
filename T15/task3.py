# --- # LOOPS EXERCISES # ---- #

# Create a while loop that will display count down from 20 to 0
number = 20
while number <= 20 and number > 0:
    number -= 1
    print(number)

# Create a loop (any) that will display all the even numbers between 1 and 20.
for i in range(1,20):
    if i % 2 == 0:
        print(i)

# Create a loop that will produce the following output: * ** *** **** *****
for item in range(1,6):
    star = item * "*"
    print(star)



# --- # CGD of POSITIVE INTEGERS # ---- #

# Compute the greatest common divisor (GCD, or highest common factor) of two positive integers.
pos_int01 = int(input("Please, insert the first positive integer: "))
pos_int02 = int(input("Please, insert the second positive integer: "))

# Define the if condition to find the 
if pos_int01 > pos_int02:  
    temp = pos_int02  
else:  
    temp = pos_int01 
# Use for loop to find the greatest common divisor of the two integers
for i in range(1, temp + 1):  
    if (( pos_int01 % i == 0) and (pos_int02 % i == 0 )):  
        gcd = i  

# Print our the solution 
print(f"The GCD of the numbers entered is: {gcd}")