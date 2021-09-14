# Generated by Django 3.2.7 on 2021-09-13 10:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.CharField(blank=True, max_length=50, primary_key=True, serialize=False, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(blank=True, max_length=25)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Models',
            fields=[
                ('id', models.CharField(blank=True, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=25)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('make_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carapi.make')),
            ],
        ),
        migrations.CreateModel(
            name='SubModel',
            fields=[
                ('id', models.CharField(blank=True, max_length=50, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=25)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('model_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carapi.models')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.CharField(blank=True, max_length=50, primary_key=True, serialize=False, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='year')),
                ('mileage', models.IntegerField(blank=True, null=True, verbose_name='mileage')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='price')),
                ('body_type', models.CharField(blank=True, max_length=25)),
                ('transmission', models.CharField(choices=[('1', 'Automatic'), ('2', 'Manual')], default='1', max_length=20)),
                ('fuel_type', models.CharField(choices=[('1', 'Petrol'), ('2', 'Diesel'), ('3', 'Hybird')], default='1', max_length=20)),
                ('exterior_color', models.CharField(blank=True, max_length=25)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('make_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carapi.make')),
                ('model_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carapi.models')),
                ('submodel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carapi.submodel')),
            ],
        ),
    ]