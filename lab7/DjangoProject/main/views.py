from django.shortcuts import render
from .models import Table1


def index(request):
    return render(request, 'main/index.html')


def main(request):
    data = {
        'title': 'Что это такое?'
    }
    return render(request, 'main/main.html', data)


def table1(request):
    tb1 = Table1.objects.all()
    return render(request, 'main/table1.html', {'table1': tb1})
