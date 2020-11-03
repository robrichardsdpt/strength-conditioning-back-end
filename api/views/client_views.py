from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.client import Client
from ..serializers import ClientSerializer, UserSerializer

# Create your views here.
class Clients(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = ClientSerializer
    def get(self, request):
        """Index request"""
        # Get all the workouts:
        # workouts = Workout.objects.all()
        # Filter the workouts by owner, so you can only see your owned workouts
        clients = Client.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = ClientSerializer(clients, many=True).data
        return Response({ 'clients': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['client']['owner'] = request.user.id
        # Serialize/create mango
        client = ClientSerializer(data=request.data['client'])
        # If the workout data is valid according to our serializer...
        if client.is_valid():
            # Save the created workout & send a response
            client.save()
            return Response({ 'client': client.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(client.errors, status=status.HTTP_400_BAD_REQUEST)

class Client_Detail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the workout to show
        client = get_object_or_404(Client, pk=pk)
        # Only want to show owned workouts?
        if not request.user.id == client.owner.id:
            raise PermissionDenied('Unauthorized, you do not work with this client')

        # Run the data through the serializer so it's formatted
        data = ClientSerializer(client).data
        return Response({ 'client': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate workout to delete
        client = get_object_or_404(Client, pk=pk)
        # Check the workout's owner agains the user making this request
        if not request.user.id == client.owner.id:
            raise PermissionDenied('Unauthorized, you do not work with this client')
        # Only delete if the user owns the  workout
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        # This "gets" the owner key on the data['workout'] dictionary
        # and returns False if it doesn't find it. So, if it's found we
        # remove it.
        if request.data['client'].get('owner', False):
            del request.data['client']['owner']

        # Locate Workout
        # get_object_or_404 returns a object representation of our Workout
        client = get_object_or_404(Client, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == client.owner.id:
            raise PermissionDenied('Unauthorized, you do not work with this client')

        # Add owner to data object now that we know this user owns the resource
        request.data['client']['owner'] = request.user.id
        # Validate updates with serializer
        data = ClientSerializer(client, data=request.data['client'])
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
