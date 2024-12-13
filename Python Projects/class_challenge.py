# Define a class
class Car:
    def __init__(self, brand, model, year):
        # Initialize the properties of the object
        self.brand = brand  # Brand of the car
        self.model = model  # Model of the car
        self.year = year    # Year the car was manufactured

    # Method to display car details
    def display_details(self):
        return f"Car Details: {self.year} {self.brand} {self.model}"

# Create an object of the Car class
my_car = Car(brand="Toyota", model="Corolla", year=2022)

# Call the method and print the result
print(my_car.display_details())
