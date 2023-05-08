from django.urls import path,include
from . import views 

urlpatterns = [
    path('', views.temp, name="the_main_home"),
    path('piano/', include('piano.urls')),
    path('bmi/', include('bmi.urls')),
    path('calculator/', include('calculator.urls')),
    path('linkshortener/', include('linkshortener.urls'), name="linkshorting"),
    path('developer/', views.ashiq, name="its_ashiq"),

]


from django.conf.urls import handler404
from bmi.views import notfound

handler404 = notfound
