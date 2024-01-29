from django.urls import path
# from auth.views import UpdateProfileView
from . import views

urlpatterns =[
    path('users/', views.CustomUserList.as_view()),
    path('users/register', views.CustomUserRegister.as_view()),
    path('user/<int:pk>/', views.CustomUserDetail.as_view()),
    path('update_profile/<int:pk>/', views.UpdateProfileView.as_view())
]