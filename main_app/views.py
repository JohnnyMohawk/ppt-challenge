from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Challenge
from .forms import PeopleForm
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
    return render(request, 'challenges/detail.html', { 'challenge': challenge, 'people_form': people_form })

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