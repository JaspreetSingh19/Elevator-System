"""
This file contain two models, 'Elevator' showing status of Elevator
and 'ElevatorRequest' showing status of requests
Both models are associated with their respective Meta class
"""

from django.db import models

from elevator.constants import FLOOR_CHOICES, REQUEST_STATUS_CHOICES
from elevator.managers.elevator import ElevatorManager
from elevator.managers.elevator_request import ElevatorRequestManager
from elevator.managers.floor_request import FloorRequestManager


class TimeStampedModel(models.Model):
    """
    An abstract model that provides fields for tracking creation and update times.

    Fields:
        created_at (datetime): The datetime when the object was created.
        updated_at (datetime): The datetime when the object was last updated.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Meta for TimeStampedModel Model
        """
        abstract = True


class Elevator(TimeStampedModel):
    """
    The 'Elevator' model with different fields telling about
    the status of the elevator
    * elevator_name is unique
    """
    elevator_name = models.CharField(max_length=10, unique=True)
    current_floor = models.PositiveIntegerField(choices=FLOOR_CHOICES, default=1)
    is_operational = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)
    is_busy = models.BooleanField(default=False)
    is_under_maintenance = models.BooleanField(default=False)
    is_moving_up = models.BooleanField(default=True)
    is_moving_down = models.BooleanField(default=False)
    is_door_open = models.BooleanField(default=False)
    is_door_closed = models.BooleanField(default=True)
    objects = ElevatorManager()

    def __str__(self):
        """
        String representation of 'Elevator' model
        :return: elevator name
        """
        return f"Elevator {self.elevator_name}"

    class Meta:
        """
        Use the Meta class to specify the database table
        for 'Elevator' model
        """
        db_table = 'Elevator'


class ElevatorRequest(TimeStampedModel):
    """
    The 'ElevatorRequest' model with different fields telling about
    the status of the elevator's request
    """
    current_floor = models.PositiveIntegerField(choices=FLOOR_CHOICES, default=1)
    request_status = models.CharField(max_length=20, choices=REQUEST_STATUS_CHOICES, default='pending')
    objects = ElevatorRequestManager()

    def __str__(self):
        """
        String representation for ElevatorRequest
        :return: floor requested
        """
        return f"Request to floor {self.current_floor}"

    class Meta:
        """
        Use the Meta class to specify the database table
        for 'ElevatorRequest' model
        """
        db_table = 'ElevatorRequest'


class FloorRequest(TimeStampedModel):
    """
    The 'FloorRequest' model with different fields telling about
    the status of the floor's request
    """
    requested_floor = models.PositiveIntegerField(choices=FLOOR_CHOICES)
    request_status = models.CharField(max_length=20, choices=REQUEST_STATUS_CHOICES, default='pending')
    objects = FloorRequestManager()

    def __str__(self):
        """
        String representation for ElevatorRequest
        :return: floor requested
        """
        return f"Request to floor {self.requested_floor}"

    class Meta:
        """
        Use the Meta class to specify the database table
        for 'ElevatorRequest' model
        """
        db_table = 'FloorRequest'
