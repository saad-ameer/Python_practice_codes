# Implement a decorator that caches the return values of a function, so that when its called with the same arguments, the cached value is returned instead of re-executing the function.

import time

# Decorator to cache function results
def cache(func):
    """
    A decorator that caches the return values of a function.
    If the function is called with the same arguments again, 
    the cached value is returned instead of re-executing the function.
    """
    cache_value = {}  # Dictionary to store cached results

    def wrapper(*args):
        """
        Wrapper function that:
        1. Checks if the function has been called with the same arguments before.
        2. If found in cache, returns the cached result.
        3. Otherwise, calls the function, stores the result, and caches it.
        """
        if args in cache_value:  # Check if result is already cached
            print("Returning cached result...")
            return cache_value[args]  # Return cached value
        
        print("Computing new result...")  # Message when function is executed
        result = func(*args)  # Call the actual function
        cache_value[args] = result  # Store the result in cache
        return result  # Return the computed result

    return wrapper  # Return the decorated function

@cache
def long_running_func(a, b):
    """
    Simulates a long-running function by sleeping for 4 seconds.
    Returns the sum of 'a' and 'b'.
    """
    time.sleep(4)  # Simulate a slow operation
    return a + b

# Calling the function multiple times with the same and different arguments
print(long_running_func(2, 3))  # Computes new result (Takes 4 sec)
print(long_running_func(2, 3))  # Returns cached result (Instant)
print(long_running_func(4, 3))  # Computes new result (Takes 4 sec)
