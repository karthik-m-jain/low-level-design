class Dog:
    species = "Canine"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
dog1 = Dog("Buddy", 5)
dog2 = Dog("Felix", 4)

print(dog1.name, dog1.age, dog1.species)
print(dog2.name, dog2.age, dog2.species)
print(Dog.species)

Dog.species = "Canidae"
print(Dog.species)

dog1.species = "Husky"
print(Dog.species)
print(dog1.species)