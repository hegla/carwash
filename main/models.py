from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=15)
    carwashes = models.ManyToManyField('Carwash', through='Order')


class Carwash(models.Model):
    name = models.CharField(max_length=30)
    foundation_date = models.DateField()
    email = models.EmailField()
    photo = models.ImageField()
    website = models.URLField()


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
    order_number = models.CharField(max_length=10, primary_key=True)
    car_body = models.CharField(max_length=10, choices=CAR_BODY)
    interior_cleaning = models.CharField(max_length=10, choices=INTERIOR_CLEANING)
    order_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    carwash = models.ForeignKey(Carwash, on_delete=models.CASCADE)
