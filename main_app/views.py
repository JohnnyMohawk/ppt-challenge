from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Challenge
from .forms import PeopleForm, PlaceForm, ThingForm


class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def challenges_index(request):
    challenges = Challenge.objects.filter(user=request.user)
    return render(request, 'challenges/index.html', { 'challenges': challenges })

@login_required
def challenges_detail(request, challenge_id):
    challenge = Challenge.objects.get(id=challenge_id)
    people_form = PeopleForm()
    place_form = PlaceForm()
    thing_form = ThingForm()
    return render(request, 'challenges/detail.html', { 
        'challenge': challenge, 
        'people_form': people_form,
        'place_form': place_form,
        'thing_form': thing_form })

class ChallengeCreate(LoginRequiredMixin, CreateView):
    model = Challenge
    fields = '__all__'
    success_url = '/challenges/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ChallengeUpdate(LoginRequiredMixin, UpdateView):
    model = Challenge
    fields = ['inspiration', 'date']

class ChallengeDelete(LoginRequiredMixin, DeleteView):
    model = Challenge
    success_url = '/challenges/'

@login_required
def add_people(request, challenge_id):
    form = PeopleForm(request.POST)
    if form.is_valid():
        new_people = form.save(commit=False)
        new_people.challenge_id = challenge_id
        new_people.save()
    return redirect('challenges_detail', challenge_id=challenge_id)

@login_required
def add_place(request, challenge_id):
    form = PlaceForm(request.POST)
    if form.is_valid():
        new_place = form.save(commit=False)
        new_place.challenge_id = challenge_id
        new_place.save()
    return redirect('challenges_detail', challenge_id=challenge_id)

@login_required
def add_thing(request, challenge_id):
    form = ThingForm(request.POST)
    if form.is_valid():
        new_thing = form.save(commit=False)
        new_thing.challenge_id = challenge_id
        new_thing.save()
    return redirect('challenges_detail', challenge_id=challenge_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('challenges_index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)