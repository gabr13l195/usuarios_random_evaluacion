from django.urls import path
from . import views

urlpatterns = [
    # URLs principales
    path('', views.user_list, name='user_list'),
    path('search/', views.user_search, name='user_search'),
    
    # URLs de usuarios
    path('user/<str:user_uuid>/', views.user_detail, name='user_detail'),
]

