# Setting up variables
num1 = 99.23
num2 = 23
num3 = 150
string1 = "100"

# Converting variables to new types
num1 = int(num1)
num2 = float(num2)
num3 = str(num2)
string1 = int(string1)

# Creates function to prints var and its type
def print_var_and_type(var):
    print(f"{var} - type is {type(var)}")

print_var_and_type(num1)
print_var_and_type(num2)
print_var_and_type(num3)
print_var_and_type(string1)