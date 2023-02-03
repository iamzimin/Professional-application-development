from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('main', views.main, name='home'),
    path('table1', views.table1, name='table1'),
    path('table2', views.table1, name='table2'),
    path('table3', views.table1, name='table3'),
    path('table4', views.table1, name='table4'),
    path('table5', views.table1, name='table5')
]