# Classify a person's age group: Child(<13), Teenager(13-19), Adult(20-59), Senior(60+).
try:
    age = int(input("Give your age:"))

    if age < 13:
        print("You are a child")
    elif age >= 13 and age < 19:
        print("You are a Teenager")
    elif age >= 19 and age < 59:
        print("You are an Adult")
    else:
        print("You are a Senior")
except ValueError:
    print("Invalid input! Please enter a number.")


# Alternate Solution
"""age = 7

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")"""
