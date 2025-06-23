# Given a string, find the first non-repeated character.

input_str = input("Give a string to find the first non-repeated character:")

"""for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("Char is: ", char)
        break"""

# Alternate solution
char_count = {}

for char in input_str:
    char_count[char] = char_count.get(char, 0) + 1

for char in input_str:
    if char_count[char] == 1:
        print(f"First non-repeated character: {char}")
        break
else:
    print("No non-repeated character found.")
