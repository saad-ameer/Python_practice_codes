def coder(num):
    # Outer function that returns a closure (inner function)
    def code(x):
        return x ** num  # Inner function uses 'num' from the outer scope (closure)
    return code          # # Returning the inner function (closure)/ factory functions

# Creating function instances
f = coder(2)  # f stores the function returned by coder(2), i.e., code() with num = 2, f has function definition(code definition) + reference of 2(num)
g = coder(3)  # g stores the function returned by coder(3), i.e., code() with num = 3

# Calling the functions
print(f(3))  # Output: 3^2 = 9
print(g(3))  # Output: 3^3 = 27

# These two functions are different:
# - 'f' holds a reference to 'num = 2' (square function).
# - 'g' holds a reference to 'num = 3' (cube function).
# - Both maintain their own 'num' value, demonstrating closures.
