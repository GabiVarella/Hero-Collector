# Generated by Django 3.0.5 on 2020-06-18 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('power', models.CharField(choices=[('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5')], default='one', max_length=100)),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Hero')),
            ],
        ),
    ]