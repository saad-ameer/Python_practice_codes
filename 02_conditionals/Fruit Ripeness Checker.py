# Determine if a fruit is ripe, overripe, or unripe based on its color.(eg. Banana: Green-Unripe, Yellow-Ripe, Brown-Overripe)

fruit = "banana"
color = input("Give a color of banana:").strip().lower()

if fruit == "banana":
    if color =="green":
        print("Your banana is Unripe.")
    elif color == "yellow":
        print("Your banana is Ripe.")
    elif color == "brown":
        print("Your banana is Overripe.")
