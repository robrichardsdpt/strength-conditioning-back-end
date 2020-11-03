from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models.workout import Workout
from .models.exercise import Exercise
from .models.user import User
from .models.client import Client

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

# class ClientViewSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Client
#        fields = ('id', 'name', 'email', 'is_active', 'is_staff', 'has_coach')

class CoachViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'is_active', 'is_staff')

#class ClientUserSerializer(serializers.ModelSerializer):
    # This model serializer will be used for User creation
    # The login serializer also inherits from this serializer
    # in order to require certain data for login
#    class Meta:
        # get_user_model will get the user model (this is required)
        # https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#referencing-the-user-model
#        model = get_user_model()
#        fields = ('id', 'name', 'email', 'password')
#        extra_kwargs = { 'password': { 'write_only': True, 'min_length': 5 } }

    # This create method will be used for model creation
#    def create(self, validated_data):
#        return get_user_model().objects.create_user(**validated_data)

#class ClientUserRegisterSerializer(serializers.Serializer):
    # Require email, password, and password_confirmation for sign up
#    email = serializers.CharField(max_length=300, required=True)
#    name = serializers.CharField(max_length=255, required=True)
#    password = serializers.CharField(required=True)
#    password_confirmation = serializers.CharField(required=True, write_only=True)

#    def validate(self, data):
        # Ensure password & password_confirmation exist
#        if not data['password'] or not data['password_confirmation']:
#            raise serializers.ValidationError('Please include a password and password confirmation.')

        # Ensure password & password_confirmation match
#        if data['password'] != data['password_confirmation']:
#            raise serializers.ValidationError('Please make sure your passwords match.')
        # if all is well, return the data
#        return data

class UserSerializer(serializers.ModelSerializer):
    # This model serializer will be used for User creation
    # The login serializer also inherits from this serializer
    # in order to require certain data for login
    class Meta:
        # get_user_model will get the user model (this is required)
        # https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#referencing-the-user-model
        model = get_user_model()
        fields = ('id', 'name', 'email', 'password')
        extra_kwargs = { 'password': { 'write_only': True, 'min_length': 5 } }

    # This create method will be used for model creation
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

class UserRegisterSerializer(serializers.Serializer):
    # Require email, password, and password_confirmation for sign up
    email = serializers.CharField(max_length=300, required=True)
    name = serializers.CharField(max_length=255, required=True)
    password = serializers.CharField(required=True)
    password_confirmation = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        # Ensure password & password_confirmation exist
        if not data['password'] or not data['password_confirmation']:
            raise serializers.ValidationError('Please include a password and password confirmation.')

        # Ensure password & password_confirmation match
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError('Please make sure your passwords match.')
        # if all is well, return the data
        return data

class ChangePasswordSerializer(serializers.Serializer):
    model = get_user_model()
    old = serializers.CharField(required=True)
    new = serializers.CharField(required=True)
