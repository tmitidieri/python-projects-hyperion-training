temp_gt_20 = True
is_weekend = True
is_sunny = True

print("Welcome to your wardrobe assistant")

temp_gt_20 = input("Is the temperature heigher than 20 degrees celsius? (Yes or No) ").lower()
if temp_gt_20 == "no":
	temp_gt_20 = False

is_weekend = input("Is it a weekend day? (Yes or No) ").lower()
if is_weekend == "no":
	is_weekend = False

is_sunny = input("Is it sunny outside? (Yes or No) ").lower()
if is_sunny == "no":
	is_sunny = False


if temp_gt_20 == False:
	outfit1 = "a long-sleeved shirt"
else:
	outfit1 = "a short-sleeved shirt"


if is_weekend == False:
	outfit2 = "jeans"
else:
	outfit2 = "shorts"


if is_sunny == False:
	outfit3 = "a raincoat"
else:
	outfit3 = "a cap"


print(f"So, your outfit today should be {outfit1}, {outfit2} and {outfit3}. You are a superstar!")
