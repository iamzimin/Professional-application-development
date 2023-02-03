from django.shortcuts import render


def index(reuest):
    return render(reuest, 'main/index.html')


def main(reuest):
    return render(reuest, 'main/main.html')


def table1(reuest):
    return render(reuest, 'main/table1.html')
