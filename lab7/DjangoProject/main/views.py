from django.shortcuts import render
from .models import CallHistory
from .models import ClientInfo
from .models import ClientGroup
from .models import Bank
from .models import BankType
#

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


def clientInfo(request):
    ci = ClientInfo.objects.all()
    return render(request, 'main/clientInfo.html', {'clientInfo': ci})


def clientGroup(request):
    cg = ClientGroup.objects.all()
    return render(request, 'main/clientGroup.html', {'clientGroup': cg})


def bank(request):
    b = Bank.objects.all()
    return render(request, 'main/bank.html', {'bank': b})


def bankType(request):
    bt = BankType.objects.all()
    return render(request, 'main/bankType.html', {'bankType': bt})

