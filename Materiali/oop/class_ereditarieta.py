import math
from UFS02.class_shape import Shape

class Rectangle(Shape):
    def __init__(self, width, height, name="A rectangle"):
        self._width=width
        self._height=height
        self._name=name

    @property
    def perimeter(self):
        return 2*(self._height+self._width)

    @property
    def area(self):
        return self._height * self._width


class Circle(Shape):
    def __init__(self, radius):
        self._radius=radius

    @property
    def perimeter(self):
        return self._radius*math.pi*2

    @property
    def area(self):
        return math.pi * self._radius ** 2