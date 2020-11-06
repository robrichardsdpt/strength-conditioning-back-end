from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.exercise import Exercise
from ..serializers import ExerciseSerializer, UserSerializer

# Create your views here.
class Exercises(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = ExerciseSerializer
    def get(self, request):
        """Index request"""
        # Get all the exercises:
        # exercises = Exercise.objects.all()
        # Filter the exercises by owner, so you can only see your owned exercises
        exercises = Exercise.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = ExerciseSerializer(exercises, many=True).data
        return Response({ 'exercises': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['exercise']['owner'] = request.user.id
        # Serialize/create exercise
        exercise = ExerciseSerializer(data=request.data['exercise'])
        # If the mango data is valid according to our serializer...
        if exercise.is_valid():
            # Save the created mango & send a response
            exercise.save()
            return Response({ 'exercise': exercise.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(exercise.errors, status=status.HTTP_400_BAD_REQUEST)

class ExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the exercise to show
        exercise = get_object_or_404(Exercise, pk=pk)
        # Only want to show owned exercises?
        if not request.user.id == exercise.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this exercise')

        # Run the data through the serializer so it's formatted
        data = ExerciseSerializer(exercise).data
        return Response({ 'exercise': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate mango to delete
        exercise = get_object_or_404(Exercise, pk=pk)
        # Check the exercise's owner agains the user making this request
        if not request.user.id == exercise.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this exercise')
        # Only delete if the user owns the  mango
        mango.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        # This "gets" the owner key on the data['exercise'] dictionary
        # and returns False if it doesn't find it. So, if it's found we
        # remove it.
        if request.data['exercise'].get('owner', False):
            del request.data['exercise']['owner']

        # Locate Exercise
        # get_object_or_404 returns a object representation of our Exercise
        exercise = get_object_or_404(Exercise, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == exercise.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this exercise')

        # Add owner to data object now that we know this user owns the resource
        request.data['exercise']['owner'] = request.user.id
        # Validate updates with serializer
        data = ExerciseSerializer(exercise, data=request.data['exercise'])
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
