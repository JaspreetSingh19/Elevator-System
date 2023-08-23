"""
This file contains manager to perform specific operations depending on model
"""
from django.db import models


class FloorRequestManager(models.Manager):
    """
    'FloorRequestManager' to perform different operations on
    'FloorRequest' model
    """
    def create_floor_request(self, **validated_data):
        """
        Creates a new floor request object
        :param validated_data: floor request fields
        :return: Floor Request object
        """
        floor_request = self.create(**validated_data)
        return floor_request
