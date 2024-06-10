import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distance(self):
        self.distance = math.sqrt((self.x ** 2) +(self.y ** 2))
        return self.distance
    
if __name__ == "__main__":
    point = Point(3, 4)
    distance = point.distance()

print(f"The distance between({point.x},{point.y}) is {distance} units.")