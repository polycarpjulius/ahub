from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name="home"),
    path('create/', Create, name="create"),
    path('update/<str:id>', Update, name="update"),
    path('delete/<str:id>',Delete, name="delete"),
]
