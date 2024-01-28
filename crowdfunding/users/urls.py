from django.urls import path
from . import views
from users.views import ChangePasswordView

urlpatterns =[
    path('users/', views.CustomUserList.as_view()),
    path('users/register', views.CustomUserRegister.as_view()),
    path('user/<int:pk>/', views.CustomUserDetail.as_view()),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password')
]