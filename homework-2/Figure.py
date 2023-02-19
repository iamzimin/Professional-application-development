from abc import abstractmethod, ABC


class Figure(ABC):
    __text = "Пример инкапсуляции"

    def exampleSet(self, txt):
        self.__text = txt

    def exampleGet(self):
        return self.__text

    @abstractmethod
    def outputFigure(self):
        pass
