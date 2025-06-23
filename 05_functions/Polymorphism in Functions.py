# Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

def multiply(a, b):
    return a * b
print(multiply(5,3))
print(multiply('a',8))
print(multiply(6,'a'))

#Alternate Solution
"""def multiply(a, b):
    # Handle numbers normally
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a * b
    
    # Handle string repetition (string * int or int * string)
    if isinstance(a, str) and isinstance(b, int):
        return a * b
    if isinstance(b, str) and isinstance(a, int):
        return b * a
    
    # Invalid case: Both are strings
    return "Error: Cannot multiply two strings!"

# Test cases
print(multiply(5, 3))      
print(multiply('a', 8))    
print(multiply(6, 'a'))    
print(multiply('hello', 'world'))  """
