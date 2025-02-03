class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self._breed = breed
        self.__age = age
    
    def display_details(self):
        print(f"{self.name}, {self._breed}, {self.__age}")
    
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            return  "Invalid Age"
        
dog = Dog("Buddy", "Labrodar", 5)
dog.display_details()
print(dog._breed)
print(dog.get_age())

dog.set_age(3)
print(dog.get_age())