from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('main', views.main, name='home'),
    path('callHistory', views.callHistory, name='callHistory'),
    path('table2', views.callHistory, name='table2'),
    path('table3', views.callHistory, name='table3'),
    path('table4', views.callHistory, name='table4'),
    path('table5', views.callHistory, name='table5')
]