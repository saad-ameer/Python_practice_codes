# Write a generator function that yields even numbers up to a specified limit.

"""def even_generator(limit):
    for i in range(2, limit+1, 2):
        print(i)

print(even_generator(10))"""

# We want a function that runs continuously but does not return values immediately.
# Instead, it should generate values using `yield` and retain its state in memory between calls.

# `yield` allows a function to return a value while maintaining its execution state.
# This enables the function to resume from where it left off in the next call.

def even_generator(limit):
    for i in range(2, limit+1, 2):
        yield i
for num in even_generator(10):
    print(num)
