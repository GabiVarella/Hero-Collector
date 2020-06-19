from django.contrib import admin

# Register your models here.
from django.contrib import admin
# import your models here
from .models import Hero, Weapon, Enemy

# Register your models here
admin.site.register(Hero),
admin.site.register(Weapon)
admin.site.register(Enemy)