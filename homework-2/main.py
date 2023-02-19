import Figure
import Rectangle
import Triangle

if __name__ == '__main__':
    # наследование: Figure является родительским и абстрактным классом Rectangle и Triangle
    vec = [Rectangle.Rectangle(), Triangle.Triangle()]

    # полиморфизм
    for i in vec:
        i.outputFigure()
    print('\n')

    # инкапсуляция
    rect = Rectangle.Rectangle()

    print(rect.exampleGet())
    rect.exampleSet("Что-то новое")
    print(rect.exampleGet())
