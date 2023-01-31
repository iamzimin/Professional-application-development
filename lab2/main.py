import random
import numpy


def tryExept(x):
    try:
        x = int(input())
        return x
    except ValueError:
        print("Введены неверные данные")
        exit()


if __name__ == '__main__':
    X = int()
    Y = int()

    # отладка неверного ввода
    print("Введите размер матрицы X * Y")
    try:
        X = tryExept(X)
        Y = tryExept(Y)
    except ValueError:
        print("Введены неверные данные")
        exit()

    vector = numpy.array([[round(random.uniform(1, 5), 1) for j in range(Y)] for i in range(X)])

    sum = int()

    for row in vector:
        for elem in row:
            sum += elem

    b = numpy.array([])
    for row in vector:
        sumX = int()
        for number in row:
            sumX += number
        b = numpy.insert(b, len(b), [round(sumX / sum, 1)])

    vector = numpy.insert(vector, len(vector), b, axis=1)

    for i in range(len(vector)):
        for j in range(len(vector[i])):
            print(vector[i][j], end=' ')
        print()
