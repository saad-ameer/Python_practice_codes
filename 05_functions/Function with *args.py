# Write a function that takes variable number of arguments and returns their sum.

# *args can take multiple arguments

def sum_all(*args):
    """print(args) # / print(*args)
    # tuple(iterative)
    for i in args:
        print(i*2)
    return sum(args)

print(sum_all(1,2,3))
print(sum_all(5,6,7,8))
print(sum_all(10,20,30,40))"""

    print(args)
    return sum(args)

nums = list(map(int, input("Provide numbers you want to add: ").split()))

result = sum_all(*nums)

print(f"The sum of provided numbers is {result}")
