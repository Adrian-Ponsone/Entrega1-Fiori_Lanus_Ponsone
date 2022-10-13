from django.urls import path
from home import views


urlpatterns = [
    path('', views.index_bootstrap, name='index'),
    path('view_users/', views.view_users, name='view_users'),
    path('about-us/', views.about_us, name='about-us'),
    path('user_creation/', views.user_creation, name='user_creation'),
]