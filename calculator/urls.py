from django.urls import path
from . import views

urlpatterns = [
    path('',views.calchome , name="calculate" ),
]
