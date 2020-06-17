from django.shortcuts import render
from django.http import HttpResponse
from .models import Hero


# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def heroes_index(request):
    heroes = Hero.objects.all()
    return render(request, 'heroes/index.html', {'heroes' : heroes})

def heroes_detail(request, hero_id):
  hero = Hero.objects.get(id=hero_id)
  return render(request, 'heroes/detail.html', {'hero': hero})