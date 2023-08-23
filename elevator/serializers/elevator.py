"""
This file contains 3 serializers to perform CRUD operations on elevator.
Each serializer is associated with its metaclas
"""
from rest_framework import serializers

from elevator.constants import FLOOR_CHOICES
from elevator.messages import VALIDATION, MIN_LENGTH, MAX_LENGTH
from elevator.models import Elevator


class ElevatorListSerializer(serializers.ModelSerializer):
    """
    'ElevatorListSerializer' for displaying elevator details
    """

    class Meta:
        """
        Use the Meta class to specify the model and fields
        that the ElevatorListSerializer should work with
        """
        model = Elevator
        fields = ['id', 'elevator_name', 'is_operational', 'is_available', 'is_busy', 'is_under_maintenance',
                  'current_floor', 'is_moving_up', 'is_moving_down', 'is_door_open', 'is_door_closed',
                  'created_at', 'updated_at']


class ElevatorCreateSerializer(serializers.ModelSerializer):
    """
    'ElevatorCreateSerializer' to create a new 'Elevator' instance with override
    'create' method
    """
    elevator_name = serializers.CharField(
        min_length=MIN_LENGTH['elevator_name'], max_length=MAX_LENGTH['elevator_name'], required=True,
        error_messages=VALIDATION['common']
    )
    current_floor = serializers.ChoiceField(choices=FLOOR_CHOICES, default=1)
    is_operational = serializers.BooleanField(default=True)
    is_available = serializers.BooleanField(default=True)
    is_busy = serializers.BooleanField(default=False)
    is_under_maintenance = serializers.BooleanField(default=False)
    is_moving_up = serializers.BooleanField(default=True)
    is_moving_down = serializers.BooleanField(default=False)
    is_door_open = serializers.BooleanField(default=False)
    is_door_closed = serializers.BooleanField(default=True)

    def create(self, validated_data):
        """
        Override create() method to create a new 'Elevator' instance
        :param validated_data: Elevator fields
        :return: Elevator object
        """
        elevator = Elevator.objects.create_elevator(**validated_data)
        return elevator

    class Meta:
        """
        Use the Meta class to specify the model and fields
        that the ElevatorCreateSerializer should work with
        """
        model = Elevator
        fields = ['id', 'elevator_name', 'current_floor', 'is_operational', 'is_available', 'is_busy',
                  'is_under_maintenance',  'current_floor', 'is_moving_up', 'is_moving_down', 'is_door_open',
                  'is_door_closed', 'created_at']


class ElevatorUpdateSerializer(serializers.ModelSerializer):
    """
    'ElevatorUpdateSerializer' to update an existing 'Elevator' instance with override
    'update' method
    """
    elevator_name = serializers.CharField(
        min_length=MIN_LENGTH['elevator_name'], max_length=MAX_LENGTH['elevator_name'], required=True,
        error_messages=VALIDATION['common']
    )
    current_floor = serializers.ChoiceField(choices=FLOOR_CHOICES, default=1)
    is_operational = serializers.BooleanField(default=True)
    is_available = serializers.BooleanField(default=True)
    is_busy = serializers.BooleanField(default=False)
    is_under_maintenance = serializers.BooleanField(default=False)
    is_moving_up = serializers.BooleanField(default=True)
    is_moving_down = serializers.BooleanField(default=False)
    is_door_open = serializers.BooleanField(default=False)
    is_door_closed = serializers.BooleanField(default=True)

    def update(self, instance, validated_data):
        """
        Override update() method to update an existing 'Elevator' instance
        :param instance: Elevator instance
        :param validated_data: Existing Elevator fields
        :return: Updated Elevator object
        """
        Elevator.objects.update_elevator(instance, **validated_data)
        updated_elevator = Elevator.objects.get_elevator(instance)
        return updated_elevator

    class Meta:
        """
        Use the Meta class to specify the model and fields
        that the ElevatorCreateSerializer should work with
        """
        model = Elevator
        fields = ['id', 'elevator_name', 'current_floor', 'is_operational', 'is_available', 'is_busy',
                  'is_under_maintenance',  'current_floor', 'is_moving_up', 'is_moving_down', 'is_door_open',
                  'is_door_closed', 'updated_at']
