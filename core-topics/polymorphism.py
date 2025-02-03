# Runtime Polymorphism
class Dog:
    def type(self):
        print(f"Dog")
        
class Labrodar(Dog):
    def type(self):
        print("Labrodar")
        
class Beagle(Dog):
    def type(self):
        print("Beagle")
        
dog = [Dog(), Labrodar(), Beagle()]
for d in dog:
    d.type()
    
# Compile-time polymorphism
class Calc:
    def add(self, a, b = 0, c = 0):
        return a + b + c
    
calculate = Calc()
print(calculate.add(2))
print(calculate.add(2,3,4))