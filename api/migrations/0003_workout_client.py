# Generated by Django 3.0 on 2020-11-03 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201102_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='client',
            field=models.CharField(default='no client attached', max_length=100),
        ),
    ]
