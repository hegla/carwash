from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from main import models as models
from main import forms as forms
from django.urls import reverse_lazy


class CustomerListView(ListView):
    model = models.Customer
    template_name = "customer/customers.html"


class CustomerCreateView(CreateView):
    model = models.Customer
    template_name = "customer/create.html"
    form_class = forms.CustomerForm

    success_url = reverse_lazy('main:customers')


class CustomerDetailView(DetailView):
    model = models.Customer
    template_name = "customer/details.html"


class CustomerUpdateView(UpdateView):
    model = models.Customer
    template_name = "customer/update.html"
    form_class = forms.CustomerForm
    success_url = reverse_lazy('main:customers')


class CustomerDeleteView(DeleteView):
    model = models.Customer
    template_name = "customer/delete.html"
    success_url = reverse_lazy('main:customers')

