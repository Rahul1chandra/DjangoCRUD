from django.urls import path

from masterdata import views as master_view

urlpatterns = [
    path('', master_view.index, name='index'),
    path('user', master_view.UserView, name='userview'),
]