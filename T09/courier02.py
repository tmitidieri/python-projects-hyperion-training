# Ask user to enter the price of the package and the delivery distance
pack_price = int(input("Please, insert the price of the package you would like to buy: "))
deliv_dist = int(input("Please, insert the total delivery distance in km: "))

# Store the delivery costs on variables to add in the final costs
air_del_type = 0.36
freight_del_type = 0.25
gift = 15
priority_deliv = 100
standard_deliv = 20
full_insurance = 50
limit_insurance = 25

# Ask user to choose the adds-on to the delivery service
addon_del01 = int(input("Please, choose how you want us to deliver your package: \n1 - Air R0.46 per Km \n2 - Freight R0.25 per Km: "))

# Create if statements to determine the total price based on user's preferences
if addon_del01 == 1:
   subtotal01 = air_del_type * deliv_dist
elif addon_del01:
    subtotal01 = freight_del_type * deliv_dist
# Restrict user to type only 1 or 2
elif addon_del01 != 1 or 2:
    int(input("This option is not available, choose between option 1 or 2."))
else:
    int(input("Invalid input. Please, choose how you want us to deliver: \n1 - Air R0.46 per Km \n2 - Freight R0.25 per Km: "))

addon_del02 = int(input("Please, choose the type of delivery: \n1 - Priority R100.00 \n2 - Standard R20.00: "))
if addon_del02 == 1:
   subtotal02 = priority_deliv + subtotal01
elif addon_del02:
    subtotal02 = standard_deliv + subtotal01
elif addon_del02 != 1 or 2:
    int(input("This option is not available, choose between option 1 or 2."))
else:
    int(input("Ivalid input.Please, choose the type of delivery: \n1 - Priority R100.00 \n2 - Standard R20.00: "))

addon_insurance = int(input("Please, choose the insurance: \n1 - Full Insurance R50.00 \n2 - Limited Insurance R25.00: "))
if addon_insurance == 1:
   subtotal03 = full_insurance + subtotal02
elif addon_insurance:
    subtotal03 = limit_insurance + subtotal02
elif addon_insurance != 1 or 2:
    int(input("This option is not available, choose between option 1 or 2."))
else:
    int(input("Invalid input.Please, choose the insurance: \n1 - Full Insurance R50.00 \n2 - Limited Insurance R25.00: "))

addon_gift = int(input("Do you want Gift pack?: \n1 - Yes - R15.00 \n2 - No: "))
if addon_gift == 1:
   subtotal04 = gift + subtotal03
elif addon_gift:
    subtotal04 = subtotal03
elif addon_gift != 1 or 2:
    int(input("This option is not available, choose between option 1 or 2."))
else:
    int(input("Invalid input. Do you want Gift pack?: \n1 - Yes - R15.00 \n2 - No: "))

grand_total = pack_price + subtotal04

print(f"The total cost of your delivery is R{grand_total}")
