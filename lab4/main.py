from datetime import datetime
import os, os.path

class RowModel():
    idx = 0
    fio = ""
    date = ""
    text = ""

    def __init__(self, idx: int, fio: str, date: str, text: str):
        self.idx = idx
        self.fio = fio
        self.date = date
        self.text = text

    def __str__(self):
        return f"Запись №{self.idx}, {self.fio}, {self.date}, {self.text}"

    def __setattr__(self, __name, __value):
        self.__dict__[__name] = __value

class Data() :
    file_path = ""
    data = []
    pointer = 0

    def __init__(self, path):
        self.file_path = path
        self.data = self.parse(self.file_path)

    def __str__(self):
        d_str = '\n'.join([str(rm) for rm in self.data])
        return f"\n{d_str}"

    def __repr__(self):
        return f"Data({[repr(rm) for rm in self.data]})"

    def __iter__(self):
        return self

    def __next__(self):
        if self.pointer >= len(self.data):
            self.pointer = 0
            raise StopIteration
        else:
            z = self.data[self.pointer]
            self.pointer += 1
            return z

    def generator(self):
        self.pointer = 0
        while self.pointer < len(self.data):
            yield self.data[self.pointer]
            self.pointer += 1

    def FIO_sort(self):
        return list(sorted(self.data, key=lambda f: f.fio))

    def DATE_sort(self):
        return list(sorted(self.data, key=lambda f: f.date))

    def select_len(self, value):
        return [rm for rm in self.data if len(rm.text) > value]

    def add_new(self, fio, date, text):
        self.data.append(RowModel(len(self.data) + 1, fio, date, text))
        self.save(self.file_path, self.data)

    @staticmethod
    def output(vec):
        for k in vec:
            print(f"Запись №{k.idx}, {k.fio}, {k.date}, {k.text}")

    @staticmethod
    def parse(path):
        parsed = []
        with open(path, "r", encoding='utf-8') as raw_csv:
            for line in raw_csv:
                (idx, nick, text, likes) = line.replace("\n", "").split(",")
                parsed.append(RowModel(int(idx), nick, text, likes))
        return parsed

    @staticmethod
    def save(path, new_data):
        with open(path, "w", encoding='utf-8') as f:
            for rm in new_data:
                f.write(f"{rm.idx},{rm.fio},{rm.date},{rm.text}\n")


if __name__ == '__main__':
    data = Data('table.csv')

    print('\n\n\nБез сортировки' + '\n' + '_' * 128)
    print(str(data))

    print('\n\n\nИтератор' + '\n' + '_' * 128)
    for item in iter(data):
        print(item)

    print('\n\n\nГенератор' + '\n' + '_' * 128)
    for item in data.generator():
        print(item)

    print('\n\n\nСортировка по ФИО' + '\n' + '_' * 128)
    data.output(data.FIO_sort())

    print('\n\n\nСортировка по дате' + '\n' + '_' * 128)
    data.output(data.DATE_sort())

    print('\n\n\nСортировка по значению' + '\n' + '_' * 128)
    data.output(data.select_len(70))

    # добавление строки
    # data.add_new("T E S T", "2027-12-15 15:15:00", "MDA")








