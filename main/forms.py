from django import forms
import main.models as models


class CustomerForm(forms.ModelForm):

    class Meta:
        model = models.Customer
        exclude = ('carwashes',)