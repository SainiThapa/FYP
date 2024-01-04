from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('home',views.homepage,name="homepage"),
    path('log',views.log,name="log"),
    path('contact',views.contact,name="contact"),
    path('help',views.help,name="help"),
    
]
