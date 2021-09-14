from django.db import models
from django.utils import timezone


class Make(models.Model):
    id = models.CharField(max_length=50, blank=True, editable=True, unique=True, primary_key=True)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=25, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id


class Models(models.Model):
    id = models.CharField(max_length=100, blank=True, editable=True, unique=True, primary_key=True)
    name = models.CharField(max_length=25, blank=True)
    active = models.BooleanField(default=True)
    make_id = models.ForeignKey(
        Make,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SubModel(models.Model):
    id = models.CharField(max_length=50, blank=True, editable=True, unique=True, primary_key=True)
    name = models.CharField(max_length=25, blank=True)
    active = models.BooleanField(default=True)
    model_id = models.ForeignKey(
        Models,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    id = models.CharField(max_length=50, blank=True, editable=True, unique=True, primary_key=True)
    active = models.BooleanField(default=True)
    year = models.IntegerField(blank=True, null=True, verbose_name='year')
    mileage = models.IntegerField(blank=True, null=True, verbose_name='mileage')
    price = models.IntegerField(blank=True, null=True, verbose_name='price')
    make_id = models.ForeignKey(
        Make,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    model_id = models.ForeignKey(
        Models,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    submodel_id = models.ForeignKey(
        SubModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    body_type = models.CharField(max_length=25, blank=True)
    TRANSMISSION_CHOICES = (
        ('Automatic', "AUTOMATIC"),
        ('Manual', "MANUAL"),
    )
    transmission = models.CharField(
        max_length=20,
        choices=TRANSMISSION_CHOICES,
        default='Automatic'
    )
    FUEL_CHOICE = (
        ('Petrol', "PETROL"),
        ('Diesel', "DIESEL"),
        ('Hybrid', "HYBRID"),
    )
    fuel_type = models.CharField(
        max_length=20,
        choices=FUEL_CHOICE,
        default='Petrol'
    )
    exterior_color = models.CharField(max_length=25, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id