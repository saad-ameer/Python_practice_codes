# Check if a password is "Weak", "Medium", or "Strong". Criteria: <6 chars(Weak), 6-10 chars(Medium), >10 chars(Strong).

password = input("Provide your password:")

if len(password) < 6:
    strength = "weak"
elif len(password) <=10:
    strength = "medium"
else: 
    strength = "strong"

print(f"Your password strength is {strength}.")
