from django.db import models

# Create your models here.
class Bio(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    def __str__(self):
        return f"{self.name}"