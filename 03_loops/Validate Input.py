# Keep asking the user for input until they enter a number betweeen 1 and 10.

while True:
    num = int(input("Enter a value between 1 and 10: "))
    if 1 <= num <= 10:
        print("Thanks for the correct input!", num)
        break
    else: 
        print(f"{num} is not a correct input. Try again!")
