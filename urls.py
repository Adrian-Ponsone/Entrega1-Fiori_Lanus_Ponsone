from django.urls import path
from home import views

urlpatterns = [
    path('', views.index_bootstrap, name='index'),
    path('user_creation/', views.user_creation, name='user_creation'),
    path('view_users/', views.view_users, name='view_users'),
]