from django.urls import path
from .views.workout_views import Workouts, WorkoutDetail
from .views.exercise_views import Exercises, ExerciseDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword, Coaches, CoachDetail
from .views.client_views import Clients, Client_Detail

urlpatterns = [
  	# Restful routing
    path('workouts/', Workouts.as_view(), name='workouts'),
    path('workouts/<int:pk>/', WorkoutDetail.as_view(), name='workout_detail'),
    path('exercises/', Exercises.as_view(), name='exercises'),
    path('exercises/<int:pk>/', ExerciseDetail.as_view(), name='exercise_detail'),
    path('coaches/', Coaches.as_view(), name='coaches'),
    path('coaches/<int:pk>/', CoachDetail.as_view(), name='coach_detail'),
    path('clients/', Clients.as_view(), name='clients'),
    path('clients/<int:pk>/', Client_Detail.as_view(), name='client_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
