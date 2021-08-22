from django.shortcuts import render
from django.http import HttpResponse

class Challenge:
    def __init__(self, inspiration, date):
        self.inspiration = inspiration
        self.date = date

challenges = [
    Challenge('My Father', '8/22/2021'),
    Challenge('Once in a Lifetime', '8/21/2021'),
    Challenge('My Mother', '8/20/2021'),
    Challenge('My Wife', '8/19/2021')
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def challenges_index(request):
    return render(request, 'challenges/index.html', { 'challenges': challenges })