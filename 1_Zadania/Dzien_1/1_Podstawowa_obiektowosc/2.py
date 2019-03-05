import math

class Shape:
    x = 0
    y = 0
    color = None

    def describle(self):
        print(self.x, self.y, self.color)
    def distance(self, other):
        dist = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        return dist
    def __str__(self):
        return "Figura koloru {} o środku w punkcie {}, {}". format(self.color, self.x, self.y)

s = Shape()
s.x = 1
s.y = 5
s.color = "Black"
s2 = Shape()
s2.x = 10
s2.y = 18
s2.color = "Blue"
print(s2.distance(s))
print(s2.__str__())
s.describle()