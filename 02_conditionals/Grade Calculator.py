# Assign a letter grade on a students score: A(90-100), B(80-89), C(70-79), D(60-69), F(below 60)

score = int(input("Provide a score of a student:"))

if score >= 101:
    print("Please verify your grade again.")
    exit()

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is {grade}.")
