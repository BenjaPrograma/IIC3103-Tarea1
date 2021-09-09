from django.urls import path

from . import views

app_name = 'apiloader'
urlpatterns = [
    path('', views.home, name='home'),
    path('users/', views.users_display, name='users_display'),
    path('users/<int:user_id>/', views.user_info, name='user_info'),
    path('cities/', views.cities_display, name='cities_display'),
    path('cities/<city_id>/', views.city_info, name='city_info'),
    path('search/', views.search_res, name='search_res'),
]