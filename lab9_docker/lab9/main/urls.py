from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('main', views.main, name='home'),
    path('table_show/<int:idx>', views.table_view, name='table_show'),
    path('table_change/<int:idx>/<int:el>/<command>', views.table_change, name='table_change'),
    path('login', views.login, name='login'),
    path('registration', views.registration, name='registration'),
    path('logout', include('django.contrib.auth.urls'), name='logout', kwargs={'next_page': ''})
]