from point import Point

class ColorPoint:
    def _innit_(self,x,y,color):
        #raise and exception if we try to not have a number
        if not isinstance(x, (int,float)):
            raise PointException("x must be a number")
        if not isinstance(x, (int,float)):
            raise PointException("x must be a number")

        super()._init_(x, y) # this replaces the self.x and self. y
        self.color = color


    def _str_(self):
        return f"<{self.color}: {self.x}, {self.y}>"

p = ColorPoint(1,2, "red")
print(p.distance_orig())
print(p)

colors = ["red", "green", "blue", "yellow", "orange", "white", "purple"]

color_points = []
for i in range(10):
    color_points.append(
        ColorPoint(random.randint(-10,10),
                   random.randint(-10, 10),
                   random.choice(colors)))

print(color_points)
color_points.sort()
print(color_points)