x = 100  # Global variable

""" 
def func2(y):
    z = x + y  # x comes from the global scope, y is passed as a parameter.
    return z

result = func2(50)  # Calls func2 with y = 50
print(result)  # Expected output: 150
"""

""" 
def func3():
    x = 88  # Local variable x inside func3, does NOT modify global x
print(x)  # This would refer to global x, which remains 100
"""

def func3():
    global x  # Declaring x as global means we are modifying the global x
    x = 88  # This changes the value of global x

func3()  # Calls func3, which modifies x
print(x)  # Prints 88, since x was overridden globally

# Overriding global variables can lead to unexpected behavior, so it's best to avoid using `global` unless necessary.
