from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Exercise(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  name = models.CharField(max_length=100, default='no name given')
  sets = models.IntegerField(
        default=0,
        validators=[
          MinValueValidator(0)])
  repetitions = models.IntegerField(
        default=0,
        validators=[
          MinValueValidator(0)])
  rx_percentage = models.FloatField(
        default = 0,
        blank=True,
        validators = [
        MinValueValidator(0)
        ]
  )
  rx_rpe = models.IntegerField(
        default = 0,
        blank=True,
        validators = [
        MinValueValidator(0),
        MaxValueValidator(10)
        ]
  )
  weight = models.FloatField(
        default = 0,
        validators = [
          MinValueValidator(0)
        ])
  notes = models.CharField(max_length=200, blank=True)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  workout = models.ForeignKey('Workout', related_name='exercises', on_delete=models.CASCADE)

  def __str__(self):
    # This must return a string
    return f"The exercise performed as a part of {self.workout}."

  def as_dict(self):
    """Returns dictionary version of Workout models"""
    return {
        'id': self.id,
        'name': self.name,
        'sets': self.sets,
        'repetitions': self.exercise,
        'rx_percentage': self.rx_percentage,
        'rx_rpe': self.rx_rpe,
        'weight': self.weight,
        'notes': self.notes
    }
