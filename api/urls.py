from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView



urlpatterns = [
    
    path('register/',Registerview.as_view()),
    path('login/',Loginview.as_view()),
    path('api/token/',TokenObtainPairView.as_view(),name="token obtain view"),
    path('api/token/refresh/',TokenRefreshView.as_view(),name="token refresh  view")
    
]