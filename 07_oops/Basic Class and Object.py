# Create a Car class with attributes like brand and model. Then create an instance of this class.

# Defining the Car class
class Car:
    def __init__(self, brand, model): 
        """
        __init__ is the constructor method that initializes the object with attributes.
        This method is automatically called when an object of the class is created.
        """
        self.brand = brand  # 'self' allows access to instance attributes within the class.
        self.model = model

# Creating an instance of the Car class
my_car = Car("BMW", "M8")

# Printing attributes of my_car
print(my_car.brand)  # Output: BMW
print(my_car.model)  # Output: M8

# Creating another instance of the Car class
my_new_car = Car("Toyota", "Supra")

# Printing attributes of my_new_car
print(my_new_car.brand)  # Output: Toyota
print(my_new_car.model)  # Output: Supra
