class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def speak(self):
        print(f"The {self.species} named {self.name} makes a sound.")
class Dog(Animal):
    def __init__(self, name, breed):
        
        super().__init__(name, species="Dog")
        self.breed = breed
    
    def speak(self):
        print(f"The dog named {self.name} barks.")

animal = Animal("Generic Animal", "Unknown")
animal.speak()


dog = Dog("Buddy", "Golden Retriever")
dog.speak()
