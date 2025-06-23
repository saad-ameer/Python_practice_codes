# Add a class variable to Car that keeps track of the number of cars created.

# Parent Car class
class Car:
    total_car = 0  # Class variable to track the number of Car instances

    def __init__(self, brand, model):
        """
        Constructor initializes the Car object.
        The 'brand' attribute is private, and 'model' is public.
        Each time a new Car object is created, total_car is incremented.
        """
        self.__brand = brand  # Private attribute
        self.model = model  # Public attribute
        Car.total_car += 1  # Increment class variable to count instances

# Creating the first car instance
my_car = Car("BMW", "M8")

# Printing attributes of my_car
#print(my_car.__brand)  # AttributeError (private variable)
print(my_car.model)  # Output: M8

# Creating another car instance
my_new_car = Car("Toyota", "Supra")

# Printing attributes of my_new_car
#print(my_new_car.__brand)  # AttributeError (private variable)
print(my_new_car.model)  # Output: Supra

# Printing the total number of Car instances created
print(Car.total_car)  # Output: 2
