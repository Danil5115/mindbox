import math

class Shape:
    def area(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def is_right(self):
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[2] ** 2, sides[0] ** 2 + sides[1] ** 2)

#Реализация фабрики, для создания новых фигур и их создания без знания конкретного типа в compile-time
class ShapeFactory:
    @staticmethod
    def create_shape(shape_name, *args):
        if shape_name == "circle":
            return Circle(*args)
        elif shape_name == "triangle":
            return Triangle(*args)
        else:
            raise ValueError(f"Unknown shape: {shape_name}")