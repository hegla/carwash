from django.db import models
from django.urls import reverse
from mapbox_location_field.models import LocationField


class Customer(models.Model):
    name_surname = models.CharField(max_length=40)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=15)
    carwashes = models.ManyToManyField('Carwash', through='Order')

    def get_absolute_url(self):
        return reverse('main:customer', args=(self.pk,))

    def __str__(self):
        return f'{self.name_surname}({self.id})'


class Carwash(models.Model):
    name = models.CharField(max_length=30)
    foundation_date = models.DateField()
    email = models.EmailField()
    photo = models.ImageField(blank=True, upload_to='CarwashImages', null=True)
    website = models.URLField()
    location = LocationField(blank=True, null=True, map_attrs={"center": (30.522366336674224, 50.45084688302083)})

    def __str__(self):
        return f'{self.name}'

class Order(models.Model):
    CAR_BODY = (
        ('Sedan', 'Sedan'),
        ('Hatchback', 'Hatchback'),
        ('Coupe', 'Coupe'),
        ('Minivan', 'Minivan'),
        ('Cabriolet', 'Cabriolet'),
        ('Pickup', 'Pickup'),
        ('Fourgon', 'Fourgon'),
    )
    INTERIOR_CLEANING = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    car_body = models.CharField(max_length=10, choices=CAR_BODY)
    interior_cleaning = models.CharField(max_length=10, choices=INTERIOR_CLEANING)
    order_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    carwash = models.ForeignKey(Carwash, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('main:order', args=(self.pk,))
