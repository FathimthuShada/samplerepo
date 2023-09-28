from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index),
    path('contact/', views.contact),
    path('login/', views.login),
    path('about/', views.about),
    path('payment/', views.payment),
    path('register/', views.register),
    path('typography/', views.typography),
    path('logout/', views.logout),
]
