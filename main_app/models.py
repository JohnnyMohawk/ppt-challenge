from django.db import models

# Create your models here.
class Challenge(models.Model):
    inspiration = models.CharField(max_length=100)
    date = models.DateField('Challenge Date')

    def __str__(self):
        return self.date