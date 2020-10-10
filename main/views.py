from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import Http404, HttpResponse
from main import models as models
from main import forms as forms
from .feature import getFeatureCollection
import json


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


class CarwashListView(ListView):
    model = models.Carwash
    template_name = "carwash/carwashes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['geojson'] = getFeatureCollection(self.model)
        return context

class CarwashMapView(ListView):
    model = models.Carwash
    template_name = "carwash/map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['geojson'] = getFeatureCollection(self.model)
        print(context)
        return context

class CarwashCreateView(CreateView):
    model = models.Carwash
    template_name = "carwash/create.html"
    form_class = forms.CarwashForm

    success_url = reverse_lazy('main:carwashes')


class CarwashDetailView(DetailView):
    model = models.Carwash
    template_name = "carwash/details.html"


class CarwashUpdateView(UpdateView):
    model = models.Carwash
    template_name = "carwash/update.html"
    form_class = forms.CarwashForm
    success_url = reverse_lazy('main:carwashes')


class CarwashDeleteView(DeleteView):
    model = models.Carwash
    template_name = "carwash/delete.html"
    success_url = reverse_lazy('main:carwashes')


def carwash_autocomplete(request):
    if request.is_ajax():
        name_part = request.GET['name_part']
        print(request.GET)
        data = models.Carwash.objects.filter(name__icontains=name_part)[:50]
        res = [[i.name, str(reverse_lazy('main:carwash', args={i.id}))] for i in data]
        
        data = json.dumps(res)
        return HttpResponse(data, "application/json")
    else:
        raise Http404