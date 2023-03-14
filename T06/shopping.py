# Request user input for a three product's name and their price and store input in variables
prod_1 = input("Please, insert a product's name in your shopping list: ")
prod_1_price = float(input("Please, insert the price of the item: "))
prod_2 = input("Please, insert a product's name in your shopping list: ")
prod_2_price = float(input("Please, insert the price of the item: "))
prod_3 = input("Please, insert a product's name in your shopping list: ")
prod_3_price = float(input("Please, insert the price of the item: "))

# Calculate the total of all three products
total_sum = (prod_1_price + prod_2_price + prod_3_price)
print(f"The total of the three products is: {total_sum}")

# Calculate the average price of the three products 
average = (total_sum / 3)
print(f"The average price of the three products is: {average}")

# Print the sentence after calculations
print(f"The total of {prod_1}, {prod_2}, {prod_3} is £ {total_sum} and the average price of the items is £ {average}")