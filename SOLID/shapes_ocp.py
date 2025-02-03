# Software entities should be open for extension but not for modification
from abc import ABC, abstractmethod
import math

class Shape:
    def __init__(self, shape_name):
        self.shape_name = shape_name
        
    @abstractmethod
    def calculate_area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height
        
    # can add additional parameters
    def calculate_area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius):
        super().__init__('circle')
        self.radius = radius
        
    def calculate_area(self):
        return math.pi * self.radius**2
    
rect = Rectangle(3, 4)
print(rect.calculate_area())

circ = Circle(3)
print(circ.calculate_area())
        