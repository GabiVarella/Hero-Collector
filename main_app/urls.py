from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('heroes/', views.heroes_index, name='index'),
  path('heroes/<int:hero_id>/', views.heroes_detail, name='detail'),
  path('heroes/create/', views.HeroCreate.as_view(), name='heroes_create'),
  path('heroes/<int:pk>/update/', views.HeroUpdate.as_view(), name='heroes_update'),
  path('heroes/<int:pk>/delete/', views.HeroDelete.as_view(), name='heroes_delete'),
  path('heroes/<int:hero_id>/add_weapon/', views.add_weapon, name='add_weapon'),
  path('heroes/<int:hero_id>/assoc_enemy/<int:enemy_id>/', views.assoc_enemy, name='assoc_enemy'),
]