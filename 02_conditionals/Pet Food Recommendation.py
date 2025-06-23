# Recommend a type of pet food based on the pet's species and age.(eg. Dog:<2 years-Puppy Food, Cat:>5 years-Senior cat food.)

pet = input("Choose your pet from Dog or Cat:").strip().lower()
age = int(input("Provide your pet's age:"))

if pet == "dog":
    if age < 2:
        food = "Puppy food"
    else: 
        food = "Senior dog food"
if pet == "cat":
    if age > 5:
        food = "Senior cat food"
    else:
        food = "Kitten food"
print(f"We are recommending {food} for your {pet}.")
