import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        self.area = math.pi * (self.radius ** 2)
        return self.area
    
    def perimeter(self):
        self.perimeter = 2 * (math.pi * self.radius)
        return self.perimeter
    
if __name__ == "__main__":
    radius = 5
    circle = Circle(radius)
    area = circle.area()
    perimeter = circle.perimeter()

print(f"Area - {circle.area}")
print(f"Perimeter - {circle.perimeter}")