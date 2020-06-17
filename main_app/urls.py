from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('heroes/', views.heroes_index, name='index'),
  path('heroes/<int:hero_id>/', views.heroes_detail, name='detail'),

]