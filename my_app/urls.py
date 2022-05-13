from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="index"),
    path('home/', views.HomeView.as_view(), name="index"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('contract/', views.ContractView.as_view(), name="contract"),
]
