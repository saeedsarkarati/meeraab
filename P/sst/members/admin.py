# ~ /home/saeed/meeraab/P/sst/            members/admin.py
from django.contrib import admin
# Register your models here.


from .models import User
admin.site.register(User)

from .models import Agent
admin.site.register(Agent)

