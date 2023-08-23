"""
This file contains manager to perform specific operations depending on model
"""
from django.db import models


class ElevatorRequestManager(models.Manager):
    """
    'ElevatorRequestManager' to perform different operations on
    'ElevatorRequest' model
    """
    def create_elevator_request(self, **validated_data):
        """
        Creates a new elevator request object
        :param validated_data: elevator request fields
        :return: Elevator Request object
        """
        elevator_request = self.create(**validated_data)
        return elevator_request
