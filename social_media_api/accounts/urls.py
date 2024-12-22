
from django.urls import path, include
from .views import (
    RegisterView, 
    CustomTokenObtainPairView, 
    FollowUserView, 
    UnfollowUserView, 
    UserRegistrationView, 
    LoginView, 
    ProfileView
)

urlpatterns = [
    path('auth/', include([
        path('register/', RegisterView.as_view(), name='register'),
        path('login/', CustomTokenObtainPairView.as_view(), name='login'),
        path('profile/', ProfileView.as_view(), name='profile'),
    ])),
    path('users/', include([
        path('register/', UserRegistrationView.as_view(), name='user-register'),
        path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
        path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
    ])),
]
from django.urls import path
from .views import FollowUserView, UnfollowUserView

urlpatterns = [
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
]
