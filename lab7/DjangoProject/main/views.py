from django.shortcuts import render
from .models import CallHistory


def index(request):
    return render(request, 'main/index.html')


def main(request):
    data = {
        'title': 'Что это такое?'
    }
    return render(request, 'main/main.html', data)


def callHistory(request):
    ch = CallHistory.objects.all()
    return render(request, 'main/callHistory.html', {'callHistory': ch})
