from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^listing/$', views.listing, name='listing')   #### example for simple paginations ##

]



