from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

PEOPLE_TYPES = (
    ('L', 'Person to learn about:'),
    ('C', 'Person to reach out to:'),
    ('G', 'Person I am grateful for:'),
)

PLACE_TYPES = (
    ('L', 'Place to learn about:'),
    ('T', 'Place to travel to:'),
    ('G', 'Place I am grateful for:'),
)

THING_TYPES = (
    ('L', 'Something I want to learn about:'),
    ('N', 'Something I need:'),
    ('W', 'Something I want:'),
    ('G', 'Something I am grateful for:'),
    ('V', 'Something I need to vent about:'),
)

# Create your models here.
class Challenge(models.Model):
    inspiration = models.CharField(max_length=100)
    date = models.DateField('Challenge Date')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)

    def get_absolute_url(self):
        return reverse('challenges_detail', kwargs={'challenge_id': self.id})

    def done_peeps_today(self):
        return self.people_set.count() >= len(PEOPLE_TYPES)

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

class Place(models.Model):
    type = models.CharField(
        max_length=1,
        choices=PLACE_TYPES,
        default=PLACE_TYPES[0][0]
    )
    name = models.CharField(max_length=50)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_type_display()}"
        # return f"{self.get_type_display()} on {self.date}"

class Thing(models.Model):
    type = models.CharField(
        max_length=1,
        choices=THING_TYPES,
        default=THING_TYPES[0][0]
    )
    name = models.CharField(max_length=50)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_type_display()}"
        # return f"{self.get_type_display()} on {self.date}"