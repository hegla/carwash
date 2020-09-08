from django.shortcuts import render
from django.views.generic import DetailView, ListView
from main import models as models


class CustomerDetailView(DetailView):
    model = models.Customer
    template_name = 'customer.html'


class CustomerListView(ListView):
    model = models.Customer
    template_name = 'customers.html'