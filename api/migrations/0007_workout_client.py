# Generated by Django 3.0 on 2020-11-03 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20201103_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workouts', to='api.Client'),
        ),
    ]
