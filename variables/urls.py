from django.urls import path

from variables.views import *

urlpatterns = [
    path('variables/', variables),
    path('variables/<pk>/', variablesDetail)
]