from django.conf.urls import url
from dashboardApp import views

urlpatterns=[
    url("home/",views.homepage),
    url("dockerdashb/",views.dockerdashboard),
    url("/",views.homepage),
]