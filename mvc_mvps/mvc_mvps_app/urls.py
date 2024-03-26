from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('conferences/', views.ConferenceList.as_view(), name='conference-list'),
    path('conferences/<int:pk>', views.ConferenceDetail.as_view(), name='conference-detail'),
    path('teams/', views.TeamList.as_view(), name='team-list'),
    path('teams/<int:pk>', views.TeamDetail.as_view(), name='team-detail'),
    path('players/', views.PlayerList.as_view(), name='player-list'),
    path('players/<int:pk>', views.PlayerDetail.as_view(), name='player-detail')
]