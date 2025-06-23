# Add a method to the Car class that displays the full name of the car(brand and model).

# Defining the Car class
class Car:
    def __init__(self, brand, model):
        """
        Constructor (__init__ method) initializes the Car object with brand and model attributes.
        """
        self.brand = brand  # Assigns brand to the instance
        self.model = model  # Assigns model to the instance
    
    def full_car_name(self):
        """
        Method to return the full name of the car (brand + model).
        """
        return f"Your car is a {self.brand} {self.model}."

# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla")

# Printing attributes
print(my_car.brand)  # Output: Toyota
print(my_car.model)  # Output: Corolla

# Calling the method to display full car name
print(my_car.full_car_name())  # Output: Your car is a Toyota Corolla.
