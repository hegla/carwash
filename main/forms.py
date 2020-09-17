from django import forms
import main.models as models


class CustomerForm(forms.ModelForm):

    class Meta:
        model = models.Customer
        exclude = ('carwashes',)


class CarwashForm(forms.ModelForm):

    class Meta:
        model = models.Carwash
        fields = ('__all__')