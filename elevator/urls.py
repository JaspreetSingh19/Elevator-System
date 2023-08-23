from django.urls import path, include
from rest_framework.routers import DefaultRouter

from elevator.views.elevator import ElevatorViewSet
from elevator.views.elevator_request import ElevatorRequestViewSet

router = DefaultRouter()


router.register('elevators', ElevatorViewSet, basename='elevators')
router.register('elevator-requests', ElevatorRequestViewSet, basename='elevator_requests')


urlpatterns = [
    path('', include(router.urls)),
]
