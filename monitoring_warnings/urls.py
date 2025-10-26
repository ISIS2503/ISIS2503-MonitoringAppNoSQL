from django.urls import path

from .views import *

urlpatterns = [
    path('warnings/', warnings),
    path('warnings/<pk>/', warningDetail),
    path('warningsFilter/', warningsFilter),
]