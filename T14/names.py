# Require the user to enter the names of all pupils in a class. The user
# should be able to type “Stop” to indicate that the names of all the students have been entered.


pupil = ""
pupils = []
while pupil != "stop":
    pupil = input("Insert the name of each pupils in your class. Type 'Stop' if you have finished your list: ").lower()
    if pupil == "stop":
        print(f"You have {len(pupils)} students in your class.")
    else:
        pupils.append(pupil)
    