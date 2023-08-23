from rest_framework import serializers

from elevator.constants import FLOOR_CHOICES, REQUEST_STATUS_CHOICES
from elevator.models import ElevatorRequest


class ElevatorRequestListSerializer(serializers.ModelSerializer):
    """
    'ElevatorRequestListSerializer' for listing elevator's requests
    """

    class Meta:
        """
        Use the Meta class to specify the model and fields
        that the ElevatorRequestListSerializer should work with
        """
        model = ElevatorRequest
        fields = ['id', 'floor_requested', 'request_status', 'created_at', 'updated_at']


class ElevatorRequestCreateSerializer(serializers.ModelSerializer):
    """
    'ElevatorRequestCreateSerializer' to create a new 'ElevatorRequest' instance with override
    'create' method
    """
    current_floor = serializers.ChoiceField(choices=FLOOR_CHOICES)

    def create(self, validated_data):
        """
        Override create() method to create a new 'Elevator' instance
        :param validated_data: Elevator fields
        :return: Elevator object
        """
        elevator = ElevatorRequest.objects.create_elevator_request(**validated_data)
        return elevator

    class Meta:
        """
        Use the Meta class to specify the model and fields
        that the ElevatorRequestCreateSerializer should work with
        """
        model = ElevatorRequest
        fields = ['id', 'current_floor', 'created_at', 'updated_at']


