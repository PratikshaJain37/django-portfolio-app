from django.urls import path
from . import views

urlpatterns = [
    path("", views.about_index, name='about_index'),
]
