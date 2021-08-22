from django.shortcuts import render
from .models import Challenge
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
    return render(request, 'challenges/detail.html', { 'challenge': challenge })