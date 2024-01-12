from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home/', views.index, name='home'), # TODO: Erase to improve SEO [later]
    path('services/', views.index, name='services'),
    path('team/', views.index, name='team'),
    path('contact/', views.index, name='contact'),
    path("blog/", views.blog_index, name="blog_index"),
    path("blog/post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("blog/category/<category>/", views.blog_category, name="blog_category"),
]