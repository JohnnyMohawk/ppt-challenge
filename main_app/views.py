from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Challenge
from .forms import PeopleForm, PlaceForm
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def challenges_index(request):
    challenges = Challenge.objects.all()
    return render(request, 'challenges/index.html', { 'challenges': challenges })

def challenges_detail(request, challenge_id):
    challenge = Challenge.objects.get(id=challenge_id)
    people_form = PeopleForm
    place_form = PlaceForm
    return render(request, 'challenges/detail.html', { 
        'challenge': challenge, 
        'people_form': people_form,
        'place_form': place_form })

class ChallengeCreate(CreateView):
    model = Challenge
    fields = '__all__'
    success_url = '/challenges/'

class ChallengeUpdate(UpdateView):
    model = Challenge
    fields = ['inspiration', 'date']

class ChallengeDelete(DeleteView):
    model = Challenge
    success_url = '/challenges/'

def add_people(request, challenge_id):
    form = PeopleForm(request.POST)
    if form.is_valid():
        new_people = form.save(commit=False)
        new_people.challenge_id = challenge_id
        new_people.save()
    return redirect('challenges_detail', challenge_id=challenge_id)

def add_place(request, challenge_id):
    form = PlaceForm(request.POST)
    if form.is_valid():
        new_place = form.save(commit=False)
        new_place.challenge_id = challenge_id
        new_place.save()
    return redirect('challenges_detail', challenge_id=challenge_id)