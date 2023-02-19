from Figure import Figure
from IDrawable import IDrawable


class Rectangle(Figure, IDrawable):

    def outputFigure(self):
        print("Хай, я Квадрат")

    def draw(self):
        print("Нарисован Квадрат")
