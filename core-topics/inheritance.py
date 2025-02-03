# Single Inheritance
class Dog:
    def __init__(self, name):
        self.name = name
    
    def display_name(self):
        print(f"Display name: {self.name}")
        
class Labrodar(Dog):
    def sound(self):
        print("Labrodar Woofs")
        
# Multi-level inheritance
class Guidedog(Labrodar):
    def guide(self):
        print(f"{self.name} Guides the way!")

# Multiple Inheritance
class Friendly:
    def friendly(self):
        print("Friendly!")
        
class GoldenRetriever(Dog, Friendly):
    def sound(self):
        print("Golden Retriever Barks")
        
dog1 = Labrodar("Buddy")
dog1.display_name()
dog1.sound()

dog2 = Guidedog("Max")
dog2.display_name()
dog2.sound()
dog2.guide()

dog3 = GoldenRetriever("Charlie")
dog3.friendly()
dog3.sound()



