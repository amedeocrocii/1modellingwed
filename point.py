import random  # Correct import

class Point:
    def __init__(self, x, y):
        """
        Initialize a Point object.
        :param x: the x position on the axis
        :param y: the y position on the axis
        """
        self.x = x  # Define x attribute via self.x
        self.y = y  # Define y attribute via self.y

    def __str__(self):
        """
        Magic method that is called when we try to print an instance
        :return: <x,y>
        """
        return f"p({self.x}, {self.y})"

# Now we need to instantiate it!
p = Point(1, 2)
p2 = Point(2, 3)
p4 = Point(4.4, -55)

print(f"p.x={p.x} and p.y={p.y}")
print(f"p4.x={p4.x} and p4.y={p4.y}")

p.x = 20
print(f"p.x={p.x} and p.y={p.y}")
print(p)

# Create a list of 5 random points
points = []
for i in range(5):
    points.append(Point(random.randint(-10, 10),
                        random.randint(-10, 10)))

print("I got these 5 random points:")
for p in points:
    print(p)
