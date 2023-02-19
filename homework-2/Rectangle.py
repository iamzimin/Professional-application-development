import Figure


class Rectangle(Figure.Figure):
    _example = "Пример инкапсуляции"

    def outputFigure(self):
        print("Хай, я Квадрат")

    def exampleSet(self, txt):
        self._example = txt

    def exampleGet(self):
        return self._example
