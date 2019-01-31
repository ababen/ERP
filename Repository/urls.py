from django.urls import path

from . import views

app_name = 'Repository'
urlpatterns = [
    path('', views.index, name='index'),
]