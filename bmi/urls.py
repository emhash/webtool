from django.urls import path
from . import views

urlpatterns = [
    path('',views.bhome , name="bmii" ),
]
