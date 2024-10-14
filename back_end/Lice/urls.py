from django.urls import path
from Lice import views

urlpatterns = [
    path('licepositions/', views.LicePositionAPI.as_view()),
    path('skilldomains/', views.SkilldomainAPI.as_view()),
    path('skilldomains/<int:pk>/', views.SkilldomainAPI.as_view()),
    path('techniques/', views.TechniqueAPI.as_view()),
    path('techniques/<int:pk>/', views.TechniqueAPI.as_view()),
    path('fighters/', views.FighterAPI.as_view()),
    path('fighters/<int:pk>/', views.FighterAPI.as_view()),
    path('techniques_levels/', views.TechniqueLevelAPI.as_view()),

    path('tournaments/', views.TournamentAPI.as_view()),
    path('tournaments/<int:pk>/', views.TournamentAPI.as_view()),
    path('matchs/', views.MatchAPI.as_view()),
    path('rounds/', views.RoundAPI.as_view()),
    path('ennemyteams/', views.EnnemyTeamAPI.as_view()),
    path('roundperformances/', views.RoundPerformanceAPI.as_view()),
    path('roundperformances/<int:pk>/', views.RoundPerformanceAPI.as_view()),
]