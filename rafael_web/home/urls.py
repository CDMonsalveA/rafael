from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='home'),
    path('services/', views.services, name='services'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),

]