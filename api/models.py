from django.db import models

# Create your models here.

class ToDoModel(models.Model):
    task = models.TextField()
    isComplete = models.BooleanField()
    scheduleTime = models.DateTimeField(null = True)

    def __str__(self):
        return f"{task} {scheduleTime}"
