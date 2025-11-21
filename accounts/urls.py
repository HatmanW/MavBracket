# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('register/', views.register, name='register'),
    path('u/<int:user_id>/', views.user_public, name='user_public'),  # public profile
]
