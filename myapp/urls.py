from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView  # Import the custom login view

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),  # URL pattern for profile page
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),  # Use custom login view
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('add-music/', views.add_music, name='add_music'),
]
