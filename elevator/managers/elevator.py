"""
This file contains manager to perform specific operations depending on model
"""
from django.db import models


class ElevatorManager(models.Manager):
    """
    'ElevatorManager' to perform different operations on
    'Elevator' model
    """

    def get_elevator(self, instance):
        """
        To get an elevator depending on elevator id
        :param instance: elevator instance
        :return: elevator object
        """
        return self.get(id=instance.id)

    def create_elevator(self, **validated_data):
        """
        Creates a new elevator object
        :param validated_data: Elevator fields
        :return: Elevator object
        """
        elevator = self.create(**validated_data)
        return elevator

    def update_elevator(self, instance, **validated_data):
        """
        Updates an existing elevator object
        :param instance: Elevator instance
        :param validated_data: elevator fields
        :return: updated elevator object
        """
        updated_elevator = self.filter(id=instance.id).update(**validated_data)
        return updated_elevator
