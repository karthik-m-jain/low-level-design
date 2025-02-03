from abc import ABC, abstractmethod

class Dog(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def sound(self):
        pass
    
    def display_name(self):
        print(self.name)
        
class Labrodar(Dog):
    def sound(self):
        print("Barks")
        
class Beagle(Dog):
    def sound(self):
        print("Woofs")
        
dog = [Labrodar("Husky"), Beagle("Lark")]
for d in dog:
    d.display_name()
    d.sound()