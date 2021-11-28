import task_12_2_classes as cl


def main():
    point1 = cl.Point(0, 0)
    point2 = cl.Point(0, 1)
    point3 = cl.Point(1, 0)
    circle = cl.Circle(point1, 5)
    triangle = cl.Triangle(point1, point2, point3)
    print(circle.area())
    print(triangle.area())
    point4 = cl.Point(5, 5)
    square = cl.Square(point1, point4)
    print(square.area())
    print(square.perimeter())


if __name__ == '__main__':
    main()

