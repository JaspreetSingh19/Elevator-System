"""
This file contain two admins 'ElevatorAdmin' & 'ElevatorRequestAdmin'
for displaying model fields in django admin panel
"""
from django.contrib import admin

from elevator.models import Elevator, ElevatorRequest


class ElevatorAdmin(admin.ModelAdmin):
    """
    Custom admin 'ElevatorAdmin' for model 'Elevator' to register
    model in the admin panel
    """
    list_display = ('id', 'elevator_name', 'current_floor', 'is_operational', 'is_available', 'is_busy',
                    'is_under_maintenance', 'is_moving_up', 'is_moving_down', 'is_door_open', 'is_door_closed',
                    'created_at', 'updated_at')

    class Meta:
        """
        Use the Meta class to specify the model
        for 'ElevatorAdmin'
        """
        model = Elevator


class ElevatorRequestAdmin(admin.ModelAdmin):
    """
    Custom admin 'ElevatorRequestAdmin' for model 'ElevatorRequest' to register
    model in the admin panel
    """
    list_display = ('id', 'current_floor', 'request_status', 'created_at', 'updated_at')

    class Meta:
        """
        Use the Meta class to specify the model
        for 'ElevatorRequestAdmin'
        """
        model = ElevatorRequest


admin.site.register(Elevator, ElevatorAdmin)
admin.site.register(ElevatorRequest, ElevatorRequestAdmin)
