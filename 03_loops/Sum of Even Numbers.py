# Calculate the sum of even numbers up to a given number n.

n = int(input("Provide any n:"))

sum_even = 0

for i in range(1, n+1):
    if i % 2 == 0:
        sum_even += 1
print("The sum of even numbers = ", sum_even)

