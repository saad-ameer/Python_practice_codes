# Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

items = input("Give a list to check a duplicate: ").split()

unique_item = set()

for item in items:
    if item in unique_item:
        print(f"Duplicate is found: {item}!")
        break
    unique_item.add(item)
else:
    print("There are no duplicates!")
print(items)
