from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Client(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  name = models.CharField(max_length=250, default='no name given')
  email = models.EmailField(max_length=250, default='no email given', unique=False)
  squat1RM = models.IntegerField(
        default = 0,
        blank=True,
        validators = [
          MinValueValidator(0)
        ])
  squat1RM_goal = models.IntegerField(
        default = 0,
        blank=True,
        validators = [
          MinValueValidator(0)
        ])
  deadlift1RM = models.IntegerField(
        default = 0,
        blank=True,
        validators = [
          MinValueValidator(0)
        ])
  deadlift1RM_goal = models.IntegerField(
        default = 0,
        blank=True,
        validators = [
          MinValueValidator(0)
        ])
  bench1RM = models.IntegerField(
        default = 0,
        blank=True,
        validators = [
          MinValueValidator(0)
        ])
  bench1RM_goal = models.IntegerField(
        default = 0,
        blank=True,
        validators = [
          MinValueValidator(0)
        ])
  estimated_total = models.IntegerField(
        default = 0,
        blank=True,
        validators = [
          MinValueValidator(0)
        ])
  total_goal = models.IntegerField(
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

  coach = models.ForeignKey(get_user_model(), related_name='clients', default='', on_delete=models.CASCADE)

  def __str__(self):
    # This must return a string
    return f"The client {self.name} at {self.email}"

  def as_dict(self):
    """Returns dictionary version of Client models"""
    return {
        'id': self.id,
        'name': self.name,
        'email': self.email,
    }
