from django.db import models
from django.urls import reverse

PEOPLE_TYPES = (
    ('L', 'Person to learn about:'),
    ('C', 'Person to reach out to:'),
    ('G', 'Person I am grateful for:'),
)

# Create your models here.
class Challenge(models.Model):
    inspiration = models.CharField(max_length=100)
    date = models.DateField('Challenge Date')

    def __str__(self):
        return str(self.date)

    def get_absolute_url(self):
        return reverse('challenges_detail', kwargs={'challenge_id': self.id})

class People(models.Model):
    type = models.CharField(
        max_length=1,
        choices=PEOPLE_TYPES,
        default=PEOPLE_TYPES[0][0]
    )
    name = models.CharField(max_length=50)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)

    def __str__(self):
        print(self.get_type_display())
        return f"{self.get_type_display()}"
        # return f"{self.get_type_display()} on {self.date}"