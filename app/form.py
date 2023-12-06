from django import forms
from django.contrib import admin
from .models import Driverwork

class DriverworkDateRangeForm(forms.ModelForm):
    start_date = forms.DateField(widget=admin.widgets.AdminDateWidget())
    end_date = forms.DateField(widget=admin.widgets.AdminDateWidget())

    class Meta:
        model = Driverwork
        fields = '__all__'
