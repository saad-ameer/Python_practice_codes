# Write a decorator that measures the time a function takes to execute.

import time

# Decorator to measure function execution time
def timer(func):
    """
    A decorator that calculates and prints the execution time of a function.
    """
    def wrapper(*args, **kwargs):
        """
        Wrapper function that:
        1. Records the start time.
        2. Calls the original function.
        3. Records the end time.
        4. Calculates and prints the execution time.
        5. Returns the function’s result.
        """
        start = time.time()  # Step 1: Capture the start time before executing the function
        result = func(*args, **kwargs)  # Step 2: Call the actual function
        end = time.time()  # Step 3: Capture the end time after execution

        execution_time = end - start  # Step 4: Compute execution duration
        print(f"{func.__name__} ran in {execution_time:.4f} seconds")  # Step 5: Print the execution time
        
        return result  # Step 6: Return the function's original result
    return wrapper  # Step 7: Return the wrapper function (decorated version)

# Applying the timer decorator
@timer 
def example_func(n):
    """
    A function that simulates a time-consuming task by sleeping for 'n' seconds.
    """
    time.sleep(n)  # Function sleeps for 'n' seconds
    return f"Finished sleeping for {n} seconds"  # Returns a message after execution

# Calling the decorated function
print(example_func(2))  # Should print the execution time and function result
