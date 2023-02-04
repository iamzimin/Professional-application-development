from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('main', views.main, name='home'),
    path('table_show/<int:idx>', views.table_view, name='table_show')
]