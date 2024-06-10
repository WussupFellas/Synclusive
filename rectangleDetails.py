import math

class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def area(self):
        self.area = self.x * self.y
        return self.area
    
if __name__ == "__main__":
    rectangle = Rectangle(10, 2)
    area = rectangle.area()

print(f"The rectangle with the coordinates ({rectangle.x}, {rectangle.y}) has the area of {float(area)}")