from django.urls import path, include
from rest_framework.routers import DefaultRouter

from account.views.registration import RegistrationViewSet

router = DefaultRouter()

router.register('registration', RegistrationViewSet, basename='registration')


urlpatterns = [
    path('', include(router.urls)),
]
