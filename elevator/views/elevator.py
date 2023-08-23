"""
This file contains ElevatorViewSet to perform CRUD operations on 'Elevator' model.
"""
from rest_framework import viewsets, status
from rest_framework.response import Response

from elevator.constants import UPDATE, CREATE
from elevator.messages import SUCCESS_MESSAGES
from elevator.models import Elevator
from elevator.serializers.elevator import ElevatorListSerializer, ElevatorCreateSerializer, ElevatorUpdateSerializer


class ElevatorViewSet(viewsets.ModelViewSet):
    """
    The ElevatorViewSet handles 'create', 'update' and 'delete' operations for the Elevator model,
    It provides a serializer class for each action with permission class
    """
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    queryset = Elevator
    serializer_class = ElevatorListSerializer
    serializer_create_class = ElevatorCreateSerializer
    serializer_update_class = ElevatorUpdateSerializer

    def get_queryset(self):
        """
        The get_queryset method returns a queryset of Elevator Model objects
        It orders the queryset based on the elevator_name of the objects.
        :return: Elevator objects
        """
        queryset = self.queryset.objects.all().order_by('elevator_name')
        return queryset

    def get_serializer_class(self):
        """
        The get_serializer_class returns a serializer class based on the action being performed.
        For 'create' action, it returns ElevatorCreateSerializer,
        for 'update' action, it returns ElevatorUpdateSerializer,
        and for all other actions, it returns the default serializer, ElevatorListSerializer.
        :return: serializer class
        """
        if self.action == CREATE:
            return self.serializer_create_class
        if self.action == UPDATE:
            return self.serializer_update_class
        return self.serializer_class

    def list(self, request, *args, **kwargs):
        """
        The list retrieves all instances of the Elevator model.
        serializes them using the serializer returned by the get_serializer() method,
        and returns the serialized data in a Response object with a status code of 200 (OK).
        :return: Elevator instances
        """

        if not self.get_queryset().exists():
            return Response({"message": SUCCESS_MESSAGES['elevator']['no_elevators']}, status=status.HTTP_200_OK)

        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        """
        This method retrieves a single instance of the Elevator model
        using the provided primary key (pk).
        It then serializes the instance using the serializer defined for the view and
        returns the serialized data in a Response object with a status code of 200 (OK).
        :return: Single Elevator instance
        """
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """
        This method creates a new instance of the Elevator model using validated serializer data
        If the data is valid, it creates a new instance and
        returns a success response with a status code of 201.
        If the data is invalid, it returns an error response with a status code of 400.
        :return: elevator object
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response({'message': SUCCESS_MESSAGES['elevator']['created'],
                             'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """
        This method updates an existing instance of the Elevator model, based on the primary key (pk)
        using validated serializer data
        If the data is valid, it creates a new instance and
        returns a success response with a status code of 201.
        If the data is invalid, it returns an error response with a status code of 400.
        :return: updated elevator object
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.update(instance, serializer.validated_data)
            return Response({'message': SUCCESS_MESSAGES['elevator']['updated'],
                             'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        """
        This method updates an existing instance of the Elevator model, based on the primary key (pk)
        using validated serializer data
        If the data is valid, it creates a new instance and
        returns a success response with a status code of 201.
        If the data is invalid, it returns an error response with a status code of 400.
        :return: updated elevator object
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.update(instance, serializer.validated_data)
            return Response({'message': SUCCESS_MESSAGES['elevator']['updated'],
                             'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """
        This method deletes an instance of the Elevator model using the primary key
        It returns a success response with a message after the deletion is complete.
        :return: success response
        """
        instance = self.get_object()
        instance.delete()
        return Response({'message': SUCCESS_MESSAGES['elevator']['deleted']}, status=status.HTTP_200_OK)
