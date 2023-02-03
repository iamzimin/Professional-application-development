from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('main', views.main, name='home'),
    path('callHistory', views.callHistory, name='callHistory'),
    path('clientInfo', views.clientInfo, name='clientInfo'),
    path('clientGroup', views.clientGroup, name='clientGroup'),
    path('bank', views.bank, name='bank'),
    path('bankType', views.bankType, name='bankType')
]