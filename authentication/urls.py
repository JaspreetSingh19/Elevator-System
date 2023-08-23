"""
This file contains URL patterns for authentication
It uses a DefaultRouter to generate views
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from authentication.views.auth import LoginViewSet, LogoutViewSet

router = DefaultRouter()

router.register('login', LoginViewSet, basename='login')
router.register('logout', LogoutViewSet, basename='logout')

urlpatterns = [
    path('', include(router.urls)),
]
