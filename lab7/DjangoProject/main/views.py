from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.defaulttags import url
from django.contrib.auth.forms import UserCreationForm

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
    table_name = ["История обращений", "Информация о клиенте", "Группы клиентов", "Банк", "Тип банка"]

    if idx == 0:
        for m in CallHistory.objects.all():
            table.append({"id": m.id, 0: m.fio, 1: m.date, 2: m.text, 3: m.clientId, 4: m.bankId})

    elif idx == 1:
        for m in ClientInfo.objects.all():
            table.append({"id": m.id, 0: m.address, 1: m.age, 2: m.phoneNumber, 3: m.clientId})

    elif idx == 2:
        for m in ClientGroup.objects.all():
            table.append({"id": m.id, 0: m.isRelible, 1: m.isVIP, 2: m.type})

    elif idx == 3:
        for m in Bank.objects.all():
            table.append({"id": m.id, 0: m.bankName, 1: m.address, 3: ", ".join(map(str, m.bankType.all()))})

    elif idx == 4:
        for m in BankType.objects.all():
            table.append({"id": m.id, 0: m.bankType})

    return render(request, 'main/table_show.html', {'table_id': idx, 'table': table, 'names': model[idx].names, 'table_name': table_name[idx]})


def table_change(request, idx, el, command):
    forms = [CallHistoryForm, ClientInfoForm, ClientGroupForm, BankForm, BankTypeForm]
    model = [CallHistory, ClientInfo, ClientGroup, Bank, BankType]
    form = forms[idx]
    error = ''

    if request.method == "POST":
        form = forms[idx].clone(request.POST)
        if form.is_valid():
            if command == 'add':
                form.save()
            elif command == 'edit':
                editing_model = model[idx].objects.filter(id=el)[0]
                for field in form._meta.fields:
                    setattr(editing_model, field, form.cleaned_data.get(field))
                editing_model.save()
            return redirect('table_show', idx)
        else:
            error = 'Данные введены неправильно'

    if command == 'edit':
        form = forms[idx].clone_for_edit(model[idx].objects.filter(id=el)[0])

    if command == 'delete':
        model[idx].objects.filter(id=el).delete()
        return redirect('table_show', idx)

    return render(request, "main/form.html", {
        'form': form,
        'names': model[idx].names,
        'error': error})


    #
    # if command == 'delete':
    #     model[idx].objects.filter(id=el).delete()
    #     return redirect('/table_show/' + str(idx))
    #
    # elif command == 'edit':
    #     if request.method == 'POST':
    #         editing_model = model[idx].objects.filter(id=el)[0]
    #         if editing_model.is_valid():
    #             for field in form._meta.fields:
    #                 setattr(editing_model, field, form.cleaned_data.get(field))
    #             editing_model.save()
    #             return redirect('/table_show/' + str(idx))
    #         else:
    #             error = "Данные введены неправильно"
    #             return render(request, 'main/form.html',
    #                           {'form': form, 'names': model[idx].names, 'error': error})
    #     form = forms[idx].clone_for_edit(model[idx].objects.filter(id=el)[0])
    #
    # elif command == 'add':
    #     if request.method == 'POST':
    #         form = forms[idx].clone(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('/table_show/' + str(idx))
    #         else:
    #             error = "Данные введены неправильно"
    #             return render(request, 'main/form.html',
    #                           {'form': form, 'names': model[idx].names, 'error': error})
    #
    # return render(request, 'main/form.html',
    #               {'form': form, 'names': model[idx].names, 'error': error})


def login(request):
    form = CreateUserForm
    context = {
        'form': form
    }
    return render(request, 'main/login.html', context)


def registration(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form': form
    }
    return render(request, 'main/registration.html', context)


def logout(request):
    return redirect('')




