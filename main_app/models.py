from django.db import models


POWERS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)
# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=100)
    alter_ego = models.CharField(max_length=100)
    super_powers = models.CharField(max_length=100)
    arch_enemy = models.CharField(max_length=100)

    def __str__(self):
        return self.name

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

   