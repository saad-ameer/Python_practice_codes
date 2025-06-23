# Modify the Car class to encapsulate the brand attribute making it private, and provide a getter method for it.

class Car:
    def __init__(self, brand, model):
        """
        Constructor initializes the Car object.
        The 'brand' attribute is private (encapsulated).
        """
        self.__brand = brand  # Private attribute
        self.model = model  # Public attribute

    def get_brand(self):
        """
        Getter method for the private attribute 'brand'.
        """
        return self.__brand  # Accesses the private attribute safely

    def set_brand(self, new_brand):
        """
        Setter method to update the private attribute 'brand'.
        Ensures that only valid (non-empty) values are assigned.
        """
        if isinstance(new_brand, str) and new_brand.strip():  # Check for valid input
            self.__brand = new_brand
        else:
            print("Invalid brand name! It must be a non-empty string.")

# Creating an instance of the Car class
my_tesla = Car("Tesla", "Model S")

# Accessing brand using the getter method
print(my_tesla.get_brand())  # Output: Tesla

# Trying to access private attribute directly (will cause an error)
# print(my_tesla.__brand)  # AttributeError: 'Car' object has no attribute '__brand'

# Updating brand using the setter method
my_tesla.set_brand("Lucid")
print(my_tesla.get_brand())  # Output: Lucid

# Attempting to set an invalid brand name
my_tesla.set_brand("")  # Invalid input, prints an error message
