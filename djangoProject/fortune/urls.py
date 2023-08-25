from django.urls import path

from .views import spin_roulette, get_user_count, get_active_users

urlpatterns = [
    path('spin/', spin_roulette, name='spin_roulette'),
    path('logs/', get_user_count, name='get_user_count'),
    path('active_users/', get_active_users, name='get_active_users'),
]