from django.urls import path
from .views import (
    SignUpView, UserLoginView, LogoutView, 
    ProfileDetailView, ProfileUpdateView, DashboardView
)

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='core:home'), name='logout'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='edit_profile'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
