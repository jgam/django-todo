from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Todos(models.Model):
    user = models.CharField(max_length=32)
    todo = models.TextField(null=True)  # Json- serialized version
