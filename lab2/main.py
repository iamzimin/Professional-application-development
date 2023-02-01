import random
import numpy

def tryExept(x):
    try:
        x = int(input())
        return x
    except ValueError:
        print("Введены неверные данные")
        exit()

def findSum(v):
    sum = int()
    for row in vector:
        for elem in row:
            sum += elem
    return sum
def output(v):
    # Открываем файл и присваиваем его переменной
    with open("outputLab2.txt", "a+") as f:
        for row in v:
            for col in row:
                # Записываем строку в файл
                f.write(f"{col} ")
            f.write("\n")
        f.write("\n")

if __name__ == '__main__':
    X = int()
    Y = int()
    my_file = open("outputLab2.txt", "w")

    # отладка неверного ввода
    print("Введите размер матрицы X * Y")
    try:
        X = tryExept(X)
        Y = tryExept(Y)
    except ValueError:
        print("Введены неверные данные")
        exit()

    # заполнение массива рандомными числами
    vector = numpy.random.uniform(0, 5, (X, Y))

    # вывод массива
    output(vector)

    # нахождение общей суммы
    sum = findSum(vector)
    print(sum)

    # создание массива сумм строк
    b = numpy.array([])
    for row in vector:
        sumX = int()
        for number in row:
            sumX += number
        # заполнение массива сумм процентным соотношением суммы строки на общую сумму
        b = numpy.insert(b, len(b), [round(sumX / sum, 2)])

    # добавление этого массива с процентами в общий массив
    vector = numpy.insert(vector, len(vector[0]), b, axis=1)

    # вывод массива
    output(vector)
