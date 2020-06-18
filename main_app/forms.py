from django.forms import ModelForm
from .models import Weapon

class WeaponForm(ModelForm):
  class Meta:
    model = Weapon
    fields = ['name', 'description', 'power']