# Parent class - Vehicle
class Vehicle:
    def __init__(self, brand, model):
        # Initialize common attributes for all vehicles
        self.brand = brand
        self.model = model

    # Parent method that can be overridden in child classes
    def start_engine(self):
        print(f"The engine of the {self.brand} {self.model} is starting.")

# Child class - Car inherits from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, doors, fuel_type):
        # Call the parent constructor to inherit common attributes
        super().__init__(brand, model)
        # Car-specific attributes
        self.doors = doors
        self.fuel_type = fuel_type

    # Override the start_engine method to provide a custom implementation
    def start_engine(self):
        print(f"The car {self.brand} {self.model} with {self.doors} doors starts with a roar!")

# Child class - Motorcycle inherits from Vehicle
class Motorcycle(Vehicle):
    def __init__(self, brand, model, type_of_handlebars, engine_capacity):
        # Call the parent constructor to inherit common attributes
        super().__init__(brand, model)
        
        self.type_of_handlebars = type_of_handlebars
        self.engine_capacity = engine_capacity

    
    def start_engine(self):
        print(f"The motorcycle {self.brand} {self.model} with {self.engine_capacity}cc engine starts with a rev!")

# Using the classes

car = Car("Toyota", "Corolla", 4, "Petrol")

car.start_engine()

# Create a Motorcycle object
motorcycle = Motorcycle("Harley-Davidson", "Sportster", "Cruiser", 1200motorcycle.start_engine()
