from django.db import models
from django.urls import reverse


POWERS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)
# Create your models here.
class Enemy(models.Model):
    name = models.CharField(max_length=50)
    super_powers = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('enemies_detail', kwargs={'pk': self.id})


class Hero(models.Model):
    name = models.CharField(max_length=100)
    alter_ego = models.CharField(max_length=100)
    super_powers = models.CharField(max_length=100)
    arch_enemy = models.CharField(max_length=100)
    enemies = models.ManyToManyField(Enemy)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'hero_id': self.id})


class Weapon(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    power = models.CharField(
        max_length=100,
        choices = POWERS,
        default = POWERS[0][0]
    )
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    
    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.name} has {self.get_power_display()} power"

   