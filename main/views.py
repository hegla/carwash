from django.shortcuts import render
from django.views.generic import DetailView
from main import models as models


class CustomerDetailView(DetailView):
    model = models.Customer
    template_name = 'customer.html'
