from django.forms import ModelForm
from .models import People, Place, Thing

class PeopleForm(ModelForm):
    class Meta:
        model = People
        fields = ['type', 'name']

class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = ['type', 'name']

class ThingForm(ModelForm):
    class Meta:
        model = Thing
        fields = ['type', 'name']
