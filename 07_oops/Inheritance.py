# Create an Electric Car class that inherits from the car class and has an additional attribute battery-size.

# Parent Car class
class Car:
    def __init__(self, brand, model):  # Fixed constructor (__init__)
        """
        Constructor initializes the Car object with brand and model attributes.
        """
        self.brand = brand
        self.model = model

    def full_car_name(self):
        """
        Returns the full name of the car (brand + model).
        """
        return f"Your car is a {self.brand} {self.model}."

# Child class ElectricCar that inherits from Car
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        """
        Constructor initializes an ElectricCar object.
        Inherits brand and model from Car class and adds battery_size.
        """
        super().__init__(brand, model)  # Calls parent class constructor
        self.battery_size = battery_size  # Adds new attribute for battery size

# Creating an instance of ElectricCar
my_tesla = ElectricCar("Tesla", "Model S", "90 kWh")

# Printing attributes
print(my_tesla.brand)          # Output: Tesla
print(my_tesla.model)          # Output: Model S
print(my_tesla.battery_size)   # Output: 90 kWh
print(my_tesla.full_car_name())  # Output: Your car is a Tesla Model S.
