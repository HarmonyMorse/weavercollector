# Generated by Django 5.0.1 on 2024-01-16 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_power_alter_sighting_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='weaver',
            name='powers',
            field=models.ManyToManyField(to='main_app.power'),
        ),
    ]