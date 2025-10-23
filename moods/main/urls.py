from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.homePage, name='homePage'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('resources/', views.resources, name='resources'),    
    path('feedback/', views.feedback, name='feedback'),
    path('feedback/thanks/', views.feedback_thanks, name='feedback_thanks'),
    path('tools_apps/', views.tools_apps, name='tools_apps'),
    path('crisis/', views.crisis, name='crisis'),
    path('crisis_support/', views.crisis_support, name='crisis_support'),
    path('content/', views.content, name='content'),

]