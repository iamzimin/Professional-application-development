from datetime import datetime
import os, os.path

def parse_csv():
    data = {}

    with open("table.csv", "r", encoding='utf-8') as raw_csv:
        for line in raw_csv:
            (idx, fio, time, text) = line.replace("\n", "").split(",")
            data.update({int(idx): {"FIO": fio, "DATE": datetime.strptime(time, "%Y-%m-%d %H:%M:%S"), "TEXT": text}})
    return data

def FIO_sort(d):
    return dict(sorted(d.items(), key=lambda f: f[1]["FIO"]))

def DATE_sort(d):
    return dict(sorted(d.items(), key=lambda f: f[1]["DATE"]))

def select_len(d, value):
    return dict((k, v) for k, v in d.items() if len(v["TEXT"]) > value)

def output(vec):
    for k, v in vec.items():
        print(f"№{k}\nФИО: {v['FIO']}\nДата: {v['DATE']}\nТекст: {v['TEXT']}\n")
    print('\n\n\n')

def add_new_data(d, fio, date, text):
    with open("table.csv", "w", encoding='utf-8') as f:
        for k, v in d.items():
            f.write(f"{k},{v['FIO']},{v['DATE']},{v['TEXT']}\n")
        f.write(f"{len(d)+1},{fio},{date},{text}\n")
    data.update({len(d)+1: {"FIO": fio, "DATE": date, "TEXT": text}})

def directory_count(path):
    (loc, dirs, files) = next(os.walk(path))
    return len(files)


if __name__ == '__main__':
    folder_name = input("Название папки:")
    print("Количество файлов в папке:")
    print(directory_count(folder_name))

    data = parse_csv()

    print('Сортировка по фамилиям')
    output(FIO_sort(data))

    print('Сортировка по дате')
    output(DATE_sort(data))

    print('Выбор по значению')
    output(select_len(data, 80))

    add_new_data(data, "3 QT", "2023-12-15 15:15:00", "AXAXAXAXXAXAAXAXAXXAXAXAXAXAAXAXAXAXAX")
    add_new_data(data, "4 QY", "2023-12-15 15:15:00", "HAHAHAHAHHAHAHAH")
