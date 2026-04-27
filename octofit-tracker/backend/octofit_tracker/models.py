from djongo import models
from django.contrib.auth.models import AbstractUser
from bson import ObjectId

class User(AbstractUser):
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ['email']

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        verbose_name_plural = 'Teams'

class Activity(models.Model):
    user_id = models.CharField(max_length=100, default='')
    user_name = models.CharField(max_length=100, default='')
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()
    class Meta:
        verbose_name_plural = 'Activities'

class Leaderboard(models.Model):
    user_id = models.CharField(max_length=100, default='')
    user_name = models.CharField(max_length=100, default='')
    points = models.IntegerField()
    class Meta:
        verbose_name_plural = 'Leaderboard'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        verbose_name_plural = 'Workouts'
