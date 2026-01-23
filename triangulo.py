import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def distance_from_xy(self, x, y):
        return math.hypot(self.__x - x, self.__y - y)

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__points = [vertice1, vertice2, vertice3]

    def perimeter(self):
        p1, p2, p3 = self.__points

        return ( p1.distance_from_xy(p2._Point__x, p2._Point__y) + p2.distance_from_xy(p3._Point__x, p3._Point__y) + p3.distance_from_xy(p1._Point__x, p1._Point__y))

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
