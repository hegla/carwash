from django import forms
from dal import autocomplete
import main.models as models


class CustomerForm(forms.ModelForm):

    class Meta:
        model = models.Customer
        exclude = ('carwashes',)


class CarwashForm(forms.ModelForm):

    class Meta:
        model = models.Carwash
        fields = ('__all__')


class OrderForm(forms.ModelForm):

    customer = forms.ModelChoiceField(
        queryset=models.Customer.objects.all(),
        widget=autocomplete.ModelSelect2(url='main:customer-autocomplete',
        attrs={
            'data-minimum-input-length': 3,
        })
    )
    carwash = forms.ModelChoiceField(
        queryset=models.Carwash.objects.all(),
        widget=autocomplete.ModelSelect2(url='main:carwash-autocomplete',
        attrs={
            'data-minimum-input-length': 3,
        })
    )

    class Meta:
        model = models.Order
        fields = ('__all__')