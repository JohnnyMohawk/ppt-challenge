from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('challenges/', views.challenges_index, name='challenges_index'),
    path('challenges/<int:challenge_id>/', views.challenges_detail, name='challenges_detail'),
    path('challenges/create/', views.ChallengeCreate.as_view(), name='challenges_create'),
    path('challenges/<int:pk>/update/', views.ChallengeUpdate.as_view(), name='challenges_update'),
    path('challenges/<int:pk>/delete/', views.ChallengeDelete.as_view(), name='challenges_delete'),
]