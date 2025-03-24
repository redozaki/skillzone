from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.username
