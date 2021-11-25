import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Figure:
    pass


class Circle(Figure):
    def __init__(self, point: Point, radius):
        self.radius = radius
        self.x = point.x
        self.y = point.y

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * math.pow(self.radius, 2)


class Triangle(Figure):
    def __init__(self, point1: Point, point2: Point, point3: Point):
        self.x1 = point1.x
        self.y1 = point1.y
        self.x2 = point2.x
        self.y2 = point2.y
        self.x3 = point3.x
        self.y3 = point3.y

        self.__a = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        self.__b = math.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)
        self.__c = math.sqrt((self.x1 - self.x3) ** 2 + (self.y1 - self.y3) ** 2)

    def perimeter(self):

        return self.__a + self.__b + self.__c

    def area(self):

        p = (self.__a + self.__b + self.__c)/2
        s = math.sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c))
        return s


point1 = Point(0, 0)
point2 = Point(0, 1)
point3 = Point(1, 0)
circle = Circle(point1, 5)
triangle = Triangle(point1, point2, point3)
print(circle.area())
print(triangle.area())

