import random


def tsToDate(timestamp):
    daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = 1970

    daysTillNow = timestamp // (24 * 60 * 60)  # Дни с начала эпохи
    extraTime = timestamp % (24 * 60 * 60)  # Количество секунд после вычета дней с начала эпохи
    extraDays = 0  # Количество оставшихся дней после вычета лет
    isLeap = False  # Високосный год или нет

    while daysTillNow >= 365:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            isLeap = True
            if daysTillNow < 366:
                break

            daysTillNow -= 366
        else:
            daysTillNow -= 365

        year += 1

    # Включаем текущий день (для подсчета времени)
    extraDays = daysTillNow + 1

    # Счёт месяцев
    month = 0
    monthIndex = 0

    if isLeap:
        while True:
            # февраль, високосный год
            if monthIndex == 1:
                if extraDays - 29 < 0:
                    break

                month += 1
                extraDays -= 29
            else:
                if extraDays - daysInMonth[monthIndex] < 0:
                    break

                month += 1
                extraDays -= daysInMonth[monthIndex]

            monthIndex += 1
    else:
        while True:
            if extraDays - daysInMonth[monthIndex] < 0:
                break

            month += 1
            extraDays -= daysInMonth[monthIndex]
            monthIndex += 1

    # Подсчет дня
    if extraDays > 0:
        month += 1
        day = extraDays
    else:
        if month == 2 and isLeap == 1:
            day = 29
        else:
            day = daysInMonth[month - 1]

    # Подсчет времени
    hours = extraTime // (60 * 60)
    minutes = (extraTime % (60 * 60)) // 60
    seconds = (extraTime % (60 * 60)) % 60

    print(str(year) + "-" + str(month) + "-" + str(day))
    print(str(hours + 4) + ":" + str(minutes) + ":" + str(seconds))


def MinOn(listik):
    minim = listik[0]
    for i in range(len(listik)):
        if minim > listik[i]:
            minim = listik[i]
    return minim


if __name__ == "__main__":
    print("Задание 1")
    ts = 1678003932
    tsToDate(ts)
    
    print("\nЗадание 2")
    listik = []
    for i in range(random.randint(5, 10)):
        listik.append(random.randint(-10, 10))

    print("Исходный список: " + str(listik) + "\n")

    print("Если массив не отсортирован")
    print("Минимальное число с сложностью O(n): " + str(MinOn(listik)) + "\n")

    print("Если массив отсортирован")
    listik = sorted(listik)
    print(listik)
    print("Минимальное число с сложностью O(1): " + str(listik[0]) + "\n")
