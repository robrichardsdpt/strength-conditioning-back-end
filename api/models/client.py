from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Client(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  name = models.CharField(max_length=250, default='no name given')
  email = models.EmailField(max_length=250, default='no email given', unique=False)
  squat1RM = models.FloatField(
        default = 0,
        blank=True,
        validators = [
          MinValueValidator(0)
        ])
  squat1RM_goal = models.FloatField(
        default = 0,
        blank=True,
        validators = [
          MinValueValidator(0)
        ])
  deadlift1RM = models.FloatField(
        default = 0,
        blank=True,
        validators = [
          MinValueValidator(0)
        ])
  deadlift1RM_goal = models.FloatField(
        default = 0,
        blank=True,
        validators = [
          MinValueValidator(0)
        ])
  bench1RM = models.FloatField(
        default = 0,
        blank=True,
        validators = [
          MinValueValidator(0)
        ])
  bench1RM_goal = models.FloatField(
        default = 0,
        blank=True,
        validators = [
          MinValueValidator(0)
        ])
  estimated_total = models.FloatField(
        default = 0,
        blank=True,
        validators = [
          MinValueValidator(0)
        ])
  total_goal = models.FloatField(
        default = 0,
        blank=True,
        validators =[
          MinValueValidator(0)
        ])
  notes = models.CharField(max_length=200, blank=True)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE,
      default= ''
  )

  coach = models.ForeignKey('User', related_name='clients', default='', on_delete=models.CASCADE)

  def __str__(self):
    # This must return a string
    return f"The client {self.name} works with {self.coach}"

  def as_dict(self):
    """Returns dictionary version of Workout models"""
    return {
        'id': self.id,
        'name': self.name,
        'coach': self.coach,
    }
