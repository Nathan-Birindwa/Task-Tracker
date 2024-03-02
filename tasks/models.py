from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)
    time = models.DateTimeField()

    def __str__(self):
        return f"{self.task} {self.time} {self.description}"
    
