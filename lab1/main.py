import random

def tryExept(x):
    try:
        x = int(input())
        return x
    except ValueError:
        print("Введены неверные данные")
        exit()

def withLib(A, B, DeleteList):
    point = -1

    for x in range(len(A)):
        # ищем последовательность, если поинт -1, то мы нашли 1 вхождение в нечётные числа
        if point == -1:
            if A[x] % 2 == 1:
                point = x
        # иначе если элемент чётный, то мы нашли последнее вхождение в нечётные числа
        if A[x] % 2 == 0 or x + 1 >= len(A):

            # проверка нахождения на последнем элементе
            if x + 1 >= len(A):
                end = x
            else:
                end = x - 1

            # проверка существования цепочки нечетных элементов, в которых нет ни одного элемента из списка B
            isExist = False
            for y in range(point, end + 1):
                for z in range(len(B)):
                    if A[y] == B[z]:
                        isExist = True
                        break
                if isExist:
                    break

            # если не нашли таких чесел, то заносим индексы в список на уладение
            if not isExist:
                for y in range(point, end + 1):
                    DeleteList.append(y)

            point = -1

def sze(list):
    counter = 0
    for item in list:
        counter += 1
    return counter

def withoutLib(A, B, DeleteList):
    point = -1

    for x in range(sze(A)):
        if point == -1:
            if A[x] % 2 == 1:
                point = x
        if A[x] % 2 == 0 or x + 1 >= sze(A):

            if x + 1 >= sze(A):
                end = x
            else:
                end = x - 1

            isExist = False
            for y in range(point, end + 1):
                if A[y] in B:
                    isExist = True

            if not isExist:
                for z in range(point, end + 1):
                    DeleteList.append(z)

            point = -1


if __name__ == '__main__':
    A = []
    B = []
    # список для хранения индексов для удаления
    DeleteList = []
    point = -1

    print("Введите 0 для ввода с клавиатуры, 1 для ввода рандомайзером")
    _input = int()
    _input = tryExept(_input)

    print("Введите 0 без использования либ, 1 для использования либ")
    lib = int()
    lib = tryExept(lib)

    if _input == 0:
        # отладка неверного ввода
        try:
            A = list(map(int, input().split()))
            B = list(map(int, input().split()))
        except ValueError:
            print("Введены неверные данные")
            exit()
    else:
        # заполнение списка рандомными числами
        A = [random.randint(1, 10) for _ in range(10)]
        B = [random.randint(1, 10) for _ in range(4)]
        # вывод рандомных чисел из списка
        print(*A)
        print(*B)

    if lib == 0:
        withLib(A, B, DeleteList)
    else:
        withoutLib(A, B, DeleteList)

    # удаление нужных элементов
    for i in range(len(DeleteList)):
        A.pop(DeleteList[i] - i)

    # вывод списка
    print(*A)

# 3 2 7 5 2 1 2 6 3 9
# 1 2 5 4 8