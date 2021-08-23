from django.db import models
from django.urls import reverse

# Create your models here.
class Challenge(models.Model):
    inspiration = models.CharField(max_length=100)
    date = models.DateField('Challenge Date')

    def __str__(self):
        return self.date

    def get_absolute_url(self):
        return reverse('challenges_detail', kwargs={'challenge_id': self.id})