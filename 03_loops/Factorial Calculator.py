# Compute the factorial of a number using a while loop.

num = int(input("Give a number to calculate a factorial of it: "))

fact = 1

"""while num > 0:
    fact *= num
    num -= 1

print(f"Factorial of num is {fact}")"""

for i in range(1, num+1):
    fact *= num
    num -= 1

print("Factorial of a num is", fact)
