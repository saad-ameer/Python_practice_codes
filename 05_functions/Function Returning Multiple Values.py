# Create a function that returns both the area and circumference of a circle given its radius

import math
"""def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference
print(circle_stats(5))"""

def circle_stats(r):
    area = round((math.pi * r ** 2),2)
    circumference = round((2 * math.pi * r), 2)
    return area, circumference
radius = int(input("Provide a radius: "))
a, c = circle_stats(radius)
print("Area of a circle is ", a, "Circumference of a circle is", c)
