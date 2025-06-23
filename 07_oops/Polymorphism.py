# Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviours.

# Parent Car class
class Car:
    def __init__(self, brand, model):
        """
        Constructor initializes the Car object.
        The 'brand' attribute is private (encapsulated).
        """
        self.__brand = brand  # Private attribute
        self.model = model  # Public attribute

    def fuel_type(self):
        """
        Method defining fuel type for regular cars.
        This method will be overridden in ElectricCar.
        """
        return "Petrol or Diesel"  # Default fuel type for a normal car
    
# Child class ElectricCar inheriting from Car
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        """
        Constructor initializes an ElectricCar object.
        Inherits brand and model from Car class and adds battery_size.
        """
        super().__init__(brand, model)  # Calls parent constructor
        self.battery_size = battery_size  # Adds battery attribute
    
    def fuel_type(self):
        """
        Overriding the fuel_type method to define fuel type for electric cars.
        """
        return "Electric Charge"  # Different behavior from Car class

# Creating an instance of ElectricCar
my_tesla = ElectricCar("Tesla", "Model S", "90KWh")

# Calling fuel_type() - Demonstrating polymorphism
print(my_tesla.fuel_type())  # Output: Electric Charge

# Creating an instance of Car
supra = Car("Toyota", "Supra")

# Calling fuel_type() - Demonstrating polymorphism
print(supra.fuel_type())  # Output: Petrol or Diesel

# Single method (fuel_type) behaves differently in different classes (Polymorphism)
