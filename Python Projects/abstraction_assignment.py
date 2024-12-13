from abc import ABC, abstractmethod

class Animal(ABC):
    
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass
    
    def description(self):
        print(f"This is {self.name}, an animal.")

class Dog(Animal):
    
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def sound(self):
        print(f"{self.name} barks!")

dog = Dog("Buddy", "Golden Retriever")
dog.description()
dog.sound()
