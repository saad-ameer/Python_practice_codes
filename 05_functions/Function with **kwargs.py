# Create a function that accepts any number of keyword arguments and prints them in the format key: value

"""def print_kwargs(firstname, surname):
    print("Name:", firstname, "Lastname:", surname)
print_kwargs(firstname = "John, ", surname = "Cena")

# ERROR: print_kwargs(firstname = "Bruce,")
print_kwargs(firstname= "Bruce,", surname="Lee")
# ERROR: print_kwargs(firstname= "Bruce,", surname="Lee", Shoes = "Mexico 66")"""

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

print_kwargs(firstname = "Bruce,")
print_kwargs(firstname= "Bruce,", surname="Lee")
print_kwargs(firstname= "Bruce,", surname="Lee", Shoes = "Mexico 66")
