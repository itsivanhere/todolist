from django.db import models

# Create your models here.
# app/models.py

from django.contrib.auth.models import User

class Task(models.Model):
    task = models.CharField(max_length=150) # notes: it’s case sensitive so don’t messed up with the function name
    description = models.TextField()
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    task_owner = models.ForeignKey (User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task