# Ask the user to enter a number less than or equal to 100.
# If they enter one above 100, ask them to try again (and continue to do so until they follow instructions).
# Once they have entered a valid number, check if it is even. If it is, multiply it by 2 and print it out. 
# If it isn't, multiply it by 3 and print it out.

num = int(input("Please, enter a number less than or equal to 100: "))

while num > 100:
    num = int(input("Invalid input, try again to enter a number less than or equal to 100: "))
    continue
while num <= 100:
    if num % 2 == 0:
        even_multi = num * 2
        print(f"The correct number entered is even and multiplied for 2 is: {even_multi}")
    elif num % 2 == 1:
        odd_multi = num * 3
        print(f"The correct number entered is odd and multiplied for 3 is: {odd_multi}")
    break

    