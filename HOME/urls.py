from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.home,name='home'),
    path("team/",views.team,name='team'),
    path("contact/",views.contact,name='contact'),
    path("urc/",views.urc,name='urc'),
    path("irdc/",views.irdc,name='irdc'),
    path("project/",views.project,name='project'),
    path("sponsor/",views.sponsor,name='sponsor'),
]
