from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Workout(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  rx_date = models.CharField(max_length=100, default='no rx date')
  overall_rpe = models.IntegerField(
        default = 0,
        blank=True,
        validators = [
        MinValueValidator(0),
        MaxValueValidator(10)
        ])
  notes = models.CharField(max_length=200, blank=True)
#  client = models.ForeignKey(
#      'Client',
#      related_name='workouts',
#      on_delete=models.CASCADE,
#      default= ''
#  )
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )


  def __str__(self):
    # This must return a string
    return f"The workout on {self.rx_date} was made by {self.owner} and set up for {self.client}."

  def as_dict(self):
    """Returns dictionary version of Workout models"""
    return {
        'id': self.id,
        'rx_date': self.date,
        'notes': self.notes,
        'exercise': self.exercise,
        'overall_rpe': self.overall_rpe
    }
