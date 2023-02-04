from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaulttags import url

from .models import *
from .forms import *


def index(request):
    return render(request, 'main/index.html')


def main(request):
    data = {
        'title': 'Что это такое?'
    }
    return render(request, 'main/main.html', data)


def table_view(request, idx):
    table = []
    model = [CallHistory, ClientInfo, ClientGroup, Bank, BankType]

    if idx == 0:
        for m in CallHistory.objects.all():
            table.append({"id": m.id, 0: m.fio, 1: m.date, 2: m.text, 3: m.clientId, 4: m.bankId})

    elif idx == 1:
        for m in ClientInfo.objects.all():
            table.append({"id": m.id, 0: m.address, 1: m.age, 2: m.phoneNumber})

    elif idx == 2:
        for m in ClientGroup.objects.all():
            table.append({"id": m.id, 0: m.isRelible, 1: m.isVIP, 2: m.type})

    elif idx == 3:
        for m in Bank.objects.all():
            table.append({"id": m.id, 0: m.bankName, 1: m.address, 3: ", ".join(map(str, m.bankType.all()))})

    elif idx == 4:
        for m in BankType.objects.all():
            table.append({"id": m.id, 0: m.bankType})

    return render(request, 'main/table_show.html', {'table_id': idx, 'table': table, 'names': model[idx].names})


def table_change(request, idx, el, command):
    form = [CallHistoryForm, ClientInfoForm, ClientGroupForm, BankForm, BankTypeForm]
    model = [CallHistory, ClientInfo, ClientGroup, Bank, BankType]

    if command == 'delete':
        #model[idx].objects.filter(id=el).delete()
        # return render(request, '/main/table_show/' + str(idx) +'.html', {})
        # return url('/main/table_show/' + str(idx) +'.html', {})
        return render(request, 'main/table_change.html', {'form': form[idx], 'names': model[idx].names, 'command': command, 'idx': idx})

    if command == 'edit':
        return render(request, 'main/table_change.html', {'form': form[idx], 'names': model[idx].names, 'command': command})

    pass
