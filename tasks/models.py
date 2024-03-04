from django.db import models

# Create your models here.
class Task(models.Model):
    

    def __str__(self):
        return f"{self.task} {self.time} {self.description}"
    
