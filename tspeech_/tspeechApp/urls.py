from django.urls import  path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('tt/', views.textInput, name='textInput'),
]