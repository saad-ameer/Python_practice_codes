# Suggest an activity based on the weather(eg. Sunny-Go for a walk, Rainy-Read a book, Snowy-Build a snowman).

weather = input("Suggest a weather is Sunny, Rainy or Snowy:").strip().lower()

"""if weather == "sunny":
    print("Weather is Sunny today go for a walk.")
elif weather == "rainy":
    print("Weather is Rainy today read a book.")
elif weather == "snowy":
    print("Weather is Snowy today build a snowman.")"""

#Alternate Solution
if weather == "sunny":
    activity = "Go for a walk."
elif weather == "rainy":
    activity = "Read a book."
elif weather == "snowy":
    activity = "Build a snowman."
print(f"Today weather is {weather}, {activity}")
