import Figure
from Rectangle import Rectangle
from Triangle import Triangle
from IDrawable import IDrawable

if __name__ == '__main__':
    # наследование: Figure является родительским и абстрактным классом Rectangle и Triangle
    vec = [Rectangle(), Triangle()]

    # полиморфизм
    for i in vec:
        i.outputFigure()
    print('\n')

    # инкапсуляция
    rect = Rectangle()
    tri = Triangle()

    print(rect.exampleGet())
    rect.exampleSet("Что-то новое")
    print(rect.exampleGet())
    print('\n')

    # интерфейс
    rect.draw()
    tri.draw()
