from Figure import Figure
from IDrawable import IDrawable


class Triangle(Figure, IDrawable):

    def outputFigure(self):
        print("Хай, я Треугольник")

    def draw(self):
        print("Нарисован Треугольник")
