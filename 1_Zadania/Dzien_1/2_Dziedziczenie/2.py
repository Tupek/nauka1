import math


class Shape:
    x = 0.0
    y = 0.0
    color = "black"

    def describe(self):
        print(self.x, self.y, self.color)
    def distance(self, other):
        dist = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        return dist
    def __str__(self):
        return "Figura koloru {} o srodku w punkcie ({},{})".format(self.color, self.x, self.y)

class Circle(Shape):
    radius = 0.0
    def __init__(self, x, y, color, radius):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        print('Circle at ({}, {}), color: {} r: {}'.format(self.x, self.y, self.color, self.radius))
    def area(self):
        return self.radius ** 2 * math.pi
    def perimeter(self):
        return self.radius * math.pi * 2

c = Circle(1, 5, "green", 10)
print(c.area())
print(c.perimeter())

s = Shape()
s.x = 5
s.y = 6
print(s.distance(c))