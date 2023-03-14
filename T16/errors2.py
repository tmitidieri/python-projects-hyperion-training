animal = "Lion"
#Syntax Error; string should be in between quotes.
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth"
#Logical Error; we need to use the f(format) method to make sure our variables are evaluated

print(full_spec)
#Syntax Error; string argument should be in between brackets.