from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=100)
    alter_ego = models.CharField(max_length=100)
    super_powers = models.CharField(max_length=100)
    arch_enemy = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# heroes = [
#   Hero('Hulk', 'Bruce Banner', 'Super Strength Fueled by Rage', 'U.S. Military'),
#   Hero('Thor', 'Thro Odinson', 'Lord of Thunder', 'Loki'),
# ]