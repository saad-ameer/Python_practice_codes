# Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar

class Car:
    """
    Car class representing a generic car with brand and model attributes.
    """
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class ElectricCar(Car):
    """
    ElectricCar class that inherits from Car and adds battery_size attribute.
    """
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)  # Calls parent class constructor
        self.battery_size = battery_size  # New attribute for electric cars

# Creating an instance of ElectricCar
my_tesla = ElectricCar("Tesla", "Model S", "90KWh")

# Checking if my_tesla is an instance of Car
print(isinstance(my_tesla, Car))  # Output: True (ElectricCar is a subclass of Car)

# Checking if my_tesla is an instance of ElectricCar
print(isinstance(my_tesla, ElectricCar))  # Output: True (Direct instance)
