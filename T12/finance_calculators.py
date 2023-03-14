import math

# Ask user to choose which calculation they want to do
user_input = input("""Investment > to calculate the amount of interest you'll earn on your investment 
    \nBond > to calculate the amount you'll have to pay on a home loan.
    \nPlease, select one of the options above: 
""")

user_choice = user_input.lower()

if user_choice == 'investment':
    # ---- # INVESTMENT OPTION # ---- #
    # Ask user the amount of money they will deposit
    investment_p = int(input("Enter how much you want to deposit: \n"))

    # Ask user the interest rate
    investment_r = float(input("Enter only the numbers (don't use %) of the interest rate: \n")) / 100

    # Ask user the number of years they plan to invest
    investment_t = int(input("Enter how many years you plan on investing: \n"))

    # Ask user if they want 'simple' or 'compound' interest
    investment_interest = int(input("Do you want: \n1 - simple interest or \n2 - compound interest \n"))

    # Create function to calculate simple interest
    def simple_interest():
        A = round(investment_p * (1 + investment_r * investment_t),2)
        return A

    # Create function to calculate compound interest
    def compound_interest():
        A = round(investment_p * math.pow((1+investment_r),investment_t),2)
        return A

    if(investment_interest == 1):
        print(f"The total amount once the simple interest has been applied is £{simple_interest()}")
    else:
        print(f"The total amount once the compound interest has been applied is £{compound_interest()}")

elif user_choice == 'bond':
    # # ---- # BOND OPTION # ---- #
    # Ask user the present value of the house 
    bond_p = float(input("Enter how much is the present value of the house: \n"))

    # Ask user the annual interest rate 
    bond_i = float(input("Enter how much is the annual interest rate: \n")) / 100 / 12

    # Ask user the annual interest rate 
    bond_n = float(input("Enter the number of months over which the bond will be repaid: \n"))

    # Calculate how much a person will have to repay a home loan monthly
    R = round((bond_i * bond_p) / (1 - math.pow((1 + bond_i),-bond_n)),2)
    print(f"The monthly repayment you should do is £{R}")
else:
    print("Invalid Option. Try Again.")


