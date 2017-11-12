from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.login, name='index'),
    url(r'^logout/$', views.logout_view, name='index'),
    url(r'^updateEmployee/$', views.updateEmployee, name='updatEmployee'),
    url(r'^deleterecord/(?P<id>.*)/$', views.deleterecord, name="deleterecod"),
    url(r'^updaterecord/(?P<id>.*)/$', views.updaterecord, name="updaterecord"),
]


