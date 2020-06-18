from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Hero
from .forms import WeaponForm


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
  weapon_form = WeaponForm()
  return render(request, 'heroes/detail.html', {'hero': hero, 'weapon_form': weapon_form})

def add_weapon(request, hero_id):
  # create a ModelForm instance using the data in request.POST
  form = WeaponForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_weapon = form.save(commit=False)
    new_weapon.hero_id = hero_id
    new_weapon.save()
  return redirect('detail', hero_id=hero_id)

class HeroCreate(CreateView):
  model = Hero
  fields = '__all__'
  success_url = '/heroes/'


class HeroUpdate(UpdateView):
  model = Hero
  fields = ['alter_ego', 'super_powers', 'arch_enemy']

class HeroDelete(DeleteView):
  model = Hero
  success_url = '/heroes'