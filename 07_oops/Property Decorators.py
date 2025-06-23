# Use a property decorator in the Car class to make the model attribute read-only.

class Car:
    total_car = 0  # Class variable to track total cars

    def __init__(self, brand, model):
        """
        Constructor initializes the Car object.
        The 'brand' attribute is private.
        The 'model' attribute is private and read-only.
        """
        self.__brand = brand
        self.__model = model  # Private attribute for model

    @property
    def model(self):
        """
        Property method to make 'model' read-only.
        """
        return self.__model

# Creating an instance of Car
my_car = Car("Mercedes", "G Wagon")

# Trying to modify the model (this should fail)
# my_car.model = "AMG G 63"  # AttributeError: can't set attribute

Car("BMW", "M340i")  # Another instance (not used)

# Accessing the model correctly (read-only)
print(my_car.model)  # Output: G Wagon
