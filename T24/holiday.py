#--------------1--------------#

# creates function to calculate hotel costs
def hotel_cost(nights):
    each_night = 60.00
    total_amount = each_night * nights
    print(f'The price for {nights} nights at the hotel is £{total_amount}')

    return total_amount

#--------------2--------------#

# creates function to calculate plane costs based on the city and returns a proper message if the city is not included in the dict.
def plane_cost(city):
    cities_list = { 
        'London': 50,
        'Paris': 120,
        'Rome': 110,
        'Budapest': 180,
        'Madrid': 140,
        'Barcelona': 150,
        'Rio de Janeiro': 470,
        'Sao Paulo': 500
    }

    if cities_list.get(city) is None:
        return 0

    else:
        total_amount = cities_list[city]
        print(f'The round trip to {city} is costing only £{cities_list[city]}.')
        return total_amount

#--------------3--------------#

# creates function to calculate car costs
def car_rental(days):
    each_day = 30.00
    total_amount = each_day * days
    print(f'The total cost for this car during {days} days is £{total_amount}')
    return total_amount

#--------------4--------------#

def holiday_cost(hotel_nights,city,car_days):
    plane = plane_cost(city)

    if plane == 0:
        return print(f'Currently there are no holiday packages to {city}. Please, try another city.')

    else:
        hotel = hotel_cost(hotel_nights)
        car = car_rental(car_days)

        holiday_total = hotel + plane + car
        print(f'TOTAL PRICE TO GO TO {str(city).upper()} IS ONLY £{holiday_total}!')
        print()
        print()



# calling function with different options to see different outputs.
holiday_cost(3,'London',4)
holiday_cost(5,'Milan',6)
holiday_cost(10,'Rio de Janeiro',11)