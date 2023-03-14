options = ['Nuggets','Fishpie','Steak','Chips','Salad']

def menu():
    print()
    print("Check our menu today, and order your 3 favourite items")
    print(f"1 - {options[0]}")
    print(f"2 - {options[1]}")
    print(f"3 - {options[2]}")
    print(f"4 - {options[3]}")
    print(f"5 - {options[4]}")

def menu_info(item):
    while item != 0:
        if item == 1:
            print("Nuggets are being prepared")
            break
        elif item == 2:
            print("Fishpie is coming!")
            break
        elif item == 3:
            print("Steak is in the kitchen")
            break
        elif item == 4:
            print("Chips are coming")
            break
        elif item == 5:
            print("Salad yeah")
            break
        else:
            print("Invalid choice")


menu()
item1 = int(input("Enter your first option: "))
menu_info(item1)

print()
menu()
item2= int(input("Enter your second option: "))
menu_info(item2)

print()
menu()
item3= int(input("Enter your third option: "))
menu_info(item3)
print()

print(f"Order confirmation! You ordered: {options[item1-1]}, {options[item2-1]}, {options[item3-1]}")