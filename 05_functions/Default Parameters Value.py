# Write a function that greets a user. If no name is provided, it should greet with a default name.

def greet(name = "User"):
    return "Hello, " + name + "!"
name = input("Enter your name: ")
print(greet(name))
