from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path(r'^DataTest/',views.DataTest.as_view()),
]