from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('challenges/', views.challenges_index, name='challenges_index'),
    path('challenges/<int:challenge_id>/', views.challenges_detail, name='challenges_detail'),
    path('challenges/create/', views.ChallengeCreate.as_view(), name='challenges_create'),
    path('challenges/<int:pk>/update/', views.ChallengeUpdate.as_view(), name='challenges_update'),
    path('challenges/<int:pk>/delete/', views.ChallengeDelete.as_view(), name='challenges_delete'),
    path('challenges/<int:challenge_id>/add_people/', views.add_people, name='add_people'),
    path('challenges/<int:challenge_id>/add_place/', views.add_place, name='add_place'),
    path('challenges/<int:challenge_id>/add_thing/', views.add_thing, name='add_thing'),
    path('accounts/signup/', views.signup, name='signup'),
]