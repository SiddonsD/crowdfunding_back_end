from django.urls import path
from . import views
from .views import ChangePasswordView

urlpatterns =[
    path('users/', views.CustomUserList.as_view()),
    path('users/register', views.CustomUserRegister.as_view()),
    path('user/<int:pk>/', views.CustomUserDetail.as_view()),
    path('user/<int:pk>/change_password/', views.ChangePasswordView.as_view())
]