# Generated by Django 5.1.1 on 2024-10-07 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0003_remove_vehicle_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='year',
            field=models.IntegerField(default=0),
        ),
    ]