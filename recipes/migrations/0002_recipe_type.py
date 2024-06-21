# Generated by Django 3.2.25 on 2024-06-21 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='type',
            field=models.CharField(choices=[('VEG', 'Vegetarian'), ('NON-VEG', 'Non-Vegetarian')], default='VEG', max_length=8),
        ),
    ]