from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('items/', views.itemsPage, name='items'),
    path('road/', views.roadPage, name='road'),
    path('mount/', views.mountPage, name='mount'),
    path('africa/', views.africaPage, name='africa'),
    path('asia/', views.asiaPage, name='asia'),
    path('australia/', views.australiaPage, name='australia'),
    path('north-america/', views.americaPage, name='america'),
] 