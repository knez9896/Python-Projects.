# Parent class
class Animal:
    def __init__(self, name, species):
        self.name = name  # Name of the animal
        self.species = species  # Species of the animal

    def make_sound(self):
        return "Some generic animal sound"

# Child class 1
class Dog(Animal):
    def __init__(self, name, breed, is_trained):
        super().__init__(name, "Dog")  # Initialize parent class attributes
        self.breed = breed  # Breed of the dog
        self.is_trained = is_trained  # Whether the dog is trained or not

    def make_sound(self):
        return "Woof! Woof!"

    def fetch(self):
        return f"{self.name} is fetching the ball!"

# Child class 2
class Cat(Animal):
    def __init__(self, name, color, is_indoor):
        super().__init__(name, "Cat")  # Initialize parent class attributes
        self.color = color  # Color of the cat
        self.is_indoor = is_indoor  # Whether the cat is an indoor cat or not

    def make_sound(self):
        return "Meow!"

    def climb(self):
        return f"{self.name} is climbing the tree!"

# Example usage
def main():
    dog = Dog(name="Buddy", breed="Golden Retriever", is_trained=True)
    cat = Cat(name="Whiskers", color="Gray", is_indoor=True)

    print(f"{dog.name} is a {dog.breed} and says: {dog.make_sound()}")
    print(dog.fetch())

    print(f"{cat.name} is a {cat.color} cat and says: {cat.make_sound()}")
    print(cat.climb())

if __name__ == "__main__":
    main()
