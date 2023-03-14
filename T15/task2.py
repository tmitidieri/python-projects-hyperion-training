# Ask user to input a year and number of years   
initial_year = int(input("Please, insert a year with four digits to check if it's a leap year or not: "))
num_years = int(input("Enter a number of years: "))
final_year = initial_year + num_years 

for year in range(initial_year,final_year):
    # Check if the given year is or not a leap year
    if year % 4 == 0:   
        print(f"{year} is a leap year")
    else:
        print (f"{year} is not a leap year")
