username = "Cooper"  # Global variable

""" 
def func():
    username = "Murph"  # Local variable inside func()

print(username)  # Since func() is not called, the global variable 'username' is printed.
"""

""" 
def func():
    username = "Murph"
    print(username)  # Prints 'Murph' when func() is called

print(username)  # Prints global 'Cooper' before func() is executed
"""

# Since func() is not called, the global variable 'username' is printed.

""" 
def func():
    username = "Murph"
    print(username)  # Local 'username' is printed inside the function

print(username)  # Prints global 'Cooper'
func()  # Calls func(), which prints 'Murph'
"""

# This entire script runs in the global scope.
def func():
    # username = "Murph"  # This line is commented out
    print(username)  # Since 'username' is not found locally, Python looks in the global scope

print(username)  # Prints 'Cooper' (global variable)
func()  # Calls func(), which also prints 'Cooper' (global variable)

# It follows a bottom-up hierarchy: If 'username' is not found inside the function, 
# Python looks in the enclosing scopes, ultimately reaching the global scope.
