"""
This file contains ElevatorRequestViewSet to perform specific operations on 'ElevatorRequest' model.
"""

from rest_framework import viewsets, status
from rest_framework.response import Response

from elevator.constants import CREATE
from elevator.messages import SUCCESS_MESSAGES
from elevator.models import ElevatorRequest
from elevator.serializers.elevator_request import ElevatorRequestListSerializer, ElevatorRequestCreateSerializer


class ElevatorRequestViewSet(viewsets.ModelViewSet):
    """
    The ElevatorViewSet handles 'create' operations for the ElevatorRequest model,
    It provides a serializer class for each action with permission class
    """
    http_method_names = ['get', 'post']
    queryset = ElevatorRequest
    serializer_class = ElevatorRequestListSerializer
    serializer_create_class = ElevatorRequestCreateSerializer

    def get_queryset(self):
        """
        The get_queryset method returns a queryset of ElevatorRequest Model objects
        It orders the queryset based on the id of the objects.
        :return: ElevatorRequest objects
        """
        queryset = self.queryset.objects.all().order_by('-id')
        return queryset

    def get_serializer_class(self):
        """
        The get_serializer_class returns a serializer class based on the action being performed.
        For 'create' action, it returns ElevatorRequestSerializer,
        and for all other actions, it returns the default serializer, ElevatorRequestListSerializer.
        :return: serializer class
        """
        if self.action == CREATE:
            return self.serializer_create_class
        return self.serializer_class

    def list(self, request, *args, **kwargs):
        """
        The list retrieves all instances of the ElevatorRequest model.
        serializes them using the serializer returned by the get_serializer() method,
        and returns the serialized data in a Response object with a status code of 200 (OK).
        :return: ElevatorRequest instances
        """

        if not self.get_queryset().exists():
            return Response(
                {"message": SUCCESS_MESSAGES['elevator_request']['no_elevator_request']}, status=status.HTTP_200_OK
            )
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        """
        This method retrieves a single instance of the ElevatorRequest model
        using the provided primary key (pk).
        It then serializes the instance using the serializer defined for the view and
        returns the serialized data in a Response object with a status code of 200 (OK).
        :return: Single ElevatorRequest instance
        """
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """
        This method creates a new instance of the ElevatorRequest model using validated serializer data
        If the data is valid, it creates a new instance and
        returns a success response with a status code of 201.
        If the data is invalid, it returns an error response with a status code of 400.
        :return: ElevatorRequest object
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response({'message': SUCCESS_MESSAGES['elevator_request']['created'],
                             'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
