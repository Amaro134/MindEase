from django.urls import path
from . import views

urlpatterns = [
    path('', views.mood_tracker, name='mood_tracker'),
    path('log/', views.log_mood_view, name='log_mood'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
