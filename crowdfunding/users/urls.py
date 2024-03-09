from django.urls import path
from . import views

urlpatterns =[
    path('users/', views.CustomUserList.as_view()),
    path('users/register', views.CustomUserRegister.as_view()),
    path('user/<int:pk>/', views.CustomUserDetail.as_view()),
    path('user/change_password/<int:pk>/', views.ChangePasswordView.as_view()),
    path('user/update_profile/<int:pk>/', views.UpdateProfileView.as_view()),
    path('api-token-auth/', views.CustomAuthToken.as_view(), name='api_token_auth')
]
