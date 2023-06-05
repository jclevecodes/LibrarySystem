from abc import ABC, abstractmethod

class Animal(ABC):
    
    def __init__(self, name):
        self.animalName = name

    @abstractmethod
    def sayHello(self):
        print("Hello")

