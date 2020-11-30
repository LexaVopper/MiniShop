from django.contrib import admin
from django.urls import include, path
from . import views
from django.contrib.auth.views import LoginView




app_name = 'account'
urlpatterns = [
    path('register/', views.RegisterForm.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]


