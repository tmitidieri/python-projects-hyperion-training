# Create a cafe items list
menu = ['banana cake', 'espresso', 'croissant', 'tea']
# Create a dic with stock quantity
stock = {'banana cake': 10, 'espresso': 20, 'croissant': 15, 'tea': 10}
# Create a dic with price for each item in stock
price = {'banana cake': 2, 'espresso': 3, 'croissant': 2, 'tea': 2}

# Calculate the total worth stock in the cafe using list comprehension
stock_worth = sum(price[item] * stock[item] for item in menu)
print(f'The cafe stock worth is: £ {stock_worth}')