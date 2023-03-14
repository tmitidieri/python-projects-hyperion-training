import math
# Ask the user to enter the shape of the building (square, rectangular or round)
shape_building = int(input("Please, insert the shape of the building to calculate the area: \n1 - Square \n2 - Rectangular \n3 - Round: \n"))

# Ask user to prompt for the appropriate dimensions and calculate the area
if shape_building == 1:
    square_lenght = float(input("Please, insert the lenght of the square in meters: "))
    square_area = square_lenght ** 2
    print(f"The foundation of the building covers {square_area} m2.")

elif shape_building == 2:
    rectangle_lenght = float(input("Please, insert the lenght of the rectangle in meters: "))
    rectangle_width = float(input("Please, insert the width of the rectangle in meters: "))
    rectangle_area = rectangle_lenght * rectangle_width
    print(f"The foundation of the building covers {rectangle_area} m2.")

elif shape_building == 3:
    circle_radius = float(input("Please, insert the radius of the circle in meters: "))
    circle_area = round(math.pi * (circle_radius ** 2),2)
    print(f"The foundation of the building covers {circle_area} m2.")

elif shape_building != 1 or shape_building != 2 or shape_building != 3:
    input("Invalid input. Please, insert the shape of the building to calculate the area: \n1 - Square \n2 - Rectangular \n3 - Round: \n")

else:
    print("Invalid input. Try again")
