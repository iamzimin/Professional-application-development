from django.shortcuts import render


def index(reuest):
    return render(reuest, 'main/index.html')


def main(reuest):
    data = {
        'title': 'Что это такое?'
    }
    return render(reuest, 'main/main.html', data)


def table1(reuest):
    return render(reuest, 'main/table1.html')
