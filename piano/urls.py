from django.urls import path
from . import views

urlpatterns = [
    path('',views.phome, name="pianoo"),
]
