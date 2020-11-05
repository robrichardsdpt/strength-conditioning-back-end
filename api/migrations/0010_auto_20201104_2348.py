# Generated by Django 3.0 on 2020-11-04 23:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_user_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='bench1RM',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='client',
            name='bench1RM_goal',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='client',
            name='deadlift1RM',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='client',
            name='deadlift1RM_goal',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='client',
            name='estimated_total',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='client',
            name='squat1RM',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='client',
            name='squat1RM_goal',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='client',
            name='total_goal',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
