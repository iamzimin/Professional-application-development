from abc import abstractmethod, ABC


class Figure(ABC):

    @abstractmethod
    def outputFigure(self):
        pass
