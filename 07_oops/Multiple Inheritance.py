# Create two classes, Battery and Engine and let the ElectricCar class inherit from both demonstrating multiple inheritance.

# Parent class 1: Battery
class Battery:
    def battery_info(self):
        """
        Method to provide battery-related information.
        """
        return "This is a battery."

# Parent class 2: Engine
class Engine:
    def engine_info(self):
        """
        Method to provide engine-related information.
        """
        return "This is an engine."

# Child class: ElectricCar inheriting from both Battery and Engine
class ElectricCar(Battery, Engine):
    def __init__(self, brand, model):
        """
        Constructor initializes an ElectricCar object with brand and model.
        """
        self.brand = brand
        self.model = model

    def car_info(self):
        """
        Method to return car details.
        """
        return f"Electric Car: {self.brand} {self.model}"

# Creating an instance of ElectricCar
my_tesla = ElectricCar("Tesla", "Model S")

# Accessing methods from multiple parent classes
print(my_tesla.car_info())      # Output: Electric Car: Tesla Model S
print(my_tesla.engine_info())   # Output: This is an engine.
print(my_tesla.battery_info())  # Output: This is a battery.
