# Create a decorator to print the function name and the value of its arguments every time the function is called.

# Decorator to log function calls with arguments
def debug(func):
    """
    A decorator that prints the function name and its arguments 
    every time the function is called.
    """
    def wrapper(*args, **kwargs):
        """
        Wrapper function that:
        1. Extracts arguments and keyword arguments.
        2. Prints the function name along with its arguments.
        3. Calls the original function with the same arguments.
        4. Returns the function’s result.
        """
        # Convert positional arguments to a string
        args_value = ', '.join(str(arg) for arg in args) if args else "None"
        
        # Convert keyword arguments to a string
        kwargs_value = ', '.join(f"{k} = {v}" for k, v in kwargs.items()) if kwargs else "None"

        # Print function call details
        print(f"Calling: {func.__name__} with args: [{args_value}] and kwargs: [{kwargs_value}]")

        return func(*args, **kwargs)  # Call the original function
    return wrapper  # Return the decorated function

# Applying the debug decorator
@debug 
def hello():
    """Simple function that prints 'hello'"""
    print("hello")

@debug
def greet(name, greeting="Hello"):
    """Function that greets a user with a specified greeting"""
    print(f"{greeting}, {name}!")

# Calling the decorated functions
hello()
greet("Cooper", greeting="Hey")
