# ~ /home/saeed/meeraab/P/sst/           members/models.py
from django.db import models
# Create your models here.

class User(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

class Agent(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

# ~ class Wellman(User)
