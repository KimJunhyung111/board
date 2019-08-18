from django.urls import path
from . import views

urlpatterns = [
    path('home', views.blogHome, name='blogHome'),
    path('list', views.blogList, name='blogList'),
    path('detail/<int:pk>', views.blogDetail, name='blogDetail'),
    path('delete/<int:pk>', views.blogDelete, name='blogDelete'),
    path('new', views.blogNew, name='blogNew'),
    path('edit/<int:pk>', views.blogEdit, name='blogEdit'),
]