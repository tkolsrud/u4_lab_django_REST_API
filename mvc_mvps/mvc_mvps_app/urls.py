from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('conferences/', views.ConferenceList.as_view(), name='conference_list'),
    path('conferences/<int:pk>', views.ConferenceDetail.as_view(), name='conference_detail'),
    path('teams/', views.TeamList.as_view(), name='team_list'),
    path('teams/<int:pk>', views.TeamDetail.as_view(), name='team_detail'),
    path('players/', views.PlayerList.as_view(), name='player_list'),
    path('players/<int:pk>', views.PlayerDetail.as_view(), name='player_detail')
]