from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,),
    path('home',views.index),
    path('register',views.register),
    path('login',views.login),
    path('podcast',views.music),
    path('events',views.events),
    path('quiz',views.quiz),
    path('community',views.community),
    path('posts',views.posting),
    path('experiance',views.experiance),
    path('competitions',views.competitions),
]
