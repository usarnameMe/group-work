from django import forms
from .models import Vehicle
import datetime


class VehicleForm(forms.ModelForm):
    current_year = datetime.datetime.now().year
    YEAR_CHOICES = [(r, r) for r in range(1950, current_year + 1)]

    year = forms.ChoiceField(choices=YEAR_CHOICES)

    class Meta:
        model = Vehicle
        fields = ['brand', 'model', 'year', 'price', 'comments']


    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price and price < 0:
            raise forms.ValidationError("Price cannot be negative")
        return price