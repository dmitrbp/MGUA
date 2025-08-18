class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"


p1 = Point(3, 4)
p2 = Point(1, 2)

print(p1 + p2)
print(p1 - p2)
print(p1 * 2)  # scalar multiplication
print(p1 == p2)
print(p1 == Point(3, 4))
