# Reverse a string using a loop.

input_str = input("Give a string: ")

reversed_str = ""

for char in input_str:
    reversed_str = char + reversed_str
print("Here is your reversed string: ",reversed_str)
