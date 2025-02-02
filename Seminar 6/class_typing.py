class Point:
    x: int
    y: int
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"

point  = Point(10, 20)
print(f"point is {type(point)}, value = {point}")
