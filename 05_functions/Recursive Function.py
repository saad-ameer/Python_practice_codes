# Create a recursive function to calculate the factorial of a number.

def fact(n):
    if n == 0:
        return 1
    else: 
        return n * fact(n-1)
    
num = int(input("Provide a number to calculate a factorial: "))
print(f"Factorial of {num} is {fact(num)}")
