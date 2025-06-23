# Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extrashot" of espresso.

coffee_size = input("Provide a size you want Small, Medium or Large:").strip().lower()
extrashot = input("Do you want an extra shot of espresso? (yes/no):").strip().lower() == "yes"

if extrashot:
    coffee = coffee_size + " coffee with an extrashot."
else: 
    coffee = coffee_size + " coffee."
print(f"Here you have, {coffee}")
