from django.conf.urls import url
from dashboardApp import views

urlpatterns=[
    url("home/",views.dockerdashboard),
    url("/",views.dockerdashboard),
]
