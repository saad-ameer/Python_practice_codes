# Print the multiplication table for a given number upto 10, but skip the fifth iteration.

n = int(input("Provide a number for which u want a multiplication table: "))

for i in range(1, 11):
    if i == 5:
        continue
    print(n, 'x', i, '=', n*i)
