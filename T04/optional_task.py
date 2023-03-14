# Request user inputs
num1 = input("Select a number: ")
num2 = input("Select a number: ")

# Display first message
print(f" First Value {num1} - Second Value {num2} ")

# Swap values using a third and temporary variable
temp_var = num1
num1 = num2
num2 = temp_var

# Display last message
print(f" First Value {num1} - Second Value {num2} ")2