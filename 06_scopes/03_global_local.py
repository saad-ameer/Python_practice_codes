x = 100  # Global variable

""" 
def f1():
    x = 10  # Local variable inside f1
    def f2():
        print(x)  # f2() accesses x from its enclosing scope (f1)
    f2()  # Calling f2 inside f1
f1()
"""

"""
def f1():
    # x = 10  # Commented out: No local x inside f1
    def f2():
        print(x)  # Since x is not found in f1, Python looks in the global scope
    f2()  # Calling f2 inside f1
f1()  # ^ Python follows the LEGB rule (Local → Enclosing → Global → Built-in)
"""

def f1():
    x = 10  # Local variable inside f1
    def f2():
        print(x)  # f2() captures x from its enclosing scope (f1)
    return f2  # Returning f2's function definition along with its closure (not executing it)

result = f1()  # f1 executes and returns f2, but x is still remembered
result()  # Calling f2, which prints x from f1's scope (now executing f2)

# In Python, closures store variable references from their enclosing scope.
# When f1() is executed, x = 10 is created.
# When f1() returns f2, it doesn't just return its definition,
# but also "carries" (or "bags") the reference to x along with it.

# This is called a closure, where the function remembers the variables 
# from the scope in which it was created, even after that scope has finished executing.
