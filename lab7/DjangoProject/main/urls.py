from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('main', views.main, name='home'),
    path('table1', views.table1, name='table1')
]