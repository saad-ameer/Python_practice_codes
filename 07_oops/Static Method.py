# Add a static method to the Car class that returns a general description of a car.

class Car:
    """
    Car class that represents a car with a brand and model.
    Also includes a static method that returns a general description of cars.
    """
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @staticmethod
    def general_description():
        """
        Static method that provides a general description of cars.
        Since it doesn't require instance attributes, it does not use 'self'.
        """
        return "Cars are amazing inventions."

# Creating instances of Car
my_car = Car("Toyota", "Supra")
Car("Mercedes", "G Wagon")  # Another instance (not stored in a variable)

# Accessing an instance attribute
print(my_car.model)  # Output: Supra

# Calling the static method correctly (Recommended way)
print(Car.general_description())  # Output: Cars are amazing inventions.

# Alternative: Calling static method through an instance (Works but not recommended)
# print(my_car.general_description())  # Output: Cars are amazing inventions.
