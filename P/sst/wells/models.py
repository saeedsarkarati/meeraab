# ~ /home/saeed/meeraab/P/sst/         wells/models.py
from django.db import models
from members.models import User
# Create your models here.

class Well(models.Model):
	monitor = models.ForeignKey(User,
	 on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=255, default ="------")
