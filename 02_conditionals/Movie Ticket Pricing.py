# Movie tickets are priced based on age: $12 for adults(18 and over), $8 for children. Everyone gets a $2 discount on Sunday.

age = int(input("Give your age:"))
is_sunday = input("Is today is Sunday? (yes/no):").strip().lower() == "yes"

if age >= 18:
    price = 12
else:
    price = 8

if is_sunday:
    price -= 2

print(f"Your ticket price is: ${price}")


# Alternate Solution
"""day = "Sunday"

price = 12 if age >= 18 else 8
if day == "Sunday":
    price -= 2

print("Your ticket price is $",price)"""
