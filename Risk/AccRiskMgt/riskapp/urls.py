from django.conf.urls import url
from riskapp import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
]