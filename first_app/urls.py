from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('second', views.index2, name='secondname'),
]