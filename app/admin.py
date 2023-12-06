from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.contrib import admin
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.contrib import admin
from .models import Driverwork
from django import forms
from rangefilter.filter import DateRangeFilter
import csv
from .form import *
from django.shortcuts import render,redirect
from datetime import datetime
from openpyxl import Workbook
from django.http import HttpResponse
class DateRangeForm(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField()
def export_to_excel(modeladmin, request, queryset):
    # Create a new workbook
    wb = Workbook()
    ws = wb.active

    # Add headers to the worksheet (assuming you have a 'name' and 'value' field)
    ws.append(["driver id","corporate name","location","gatepass no","date","name","pick up place","drop place","vehicle no","image url"])
    Driverworks = Driverwork.objects.all()
    # Add data from the queryset to the worksheet
    for i in queryset:
        ws.append([i.driverid, i.corporatename, i.location, i.gatepassno, i.date, i.name, i.pickupplace, i.dropplace, i.vehicleno, i.imgbb_url])

    # Create a response with the Excel file
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=my_export.xlsx'

    # Save the workbook to the response
    wb.save(response)

    return response

export_to_excel.short_description = "Export selected items to Excel"

class DriverworkDateRangeForm(forms.ModelForm):
    start_date = forms.DateField(widget=admin.widgets.AdminDateWidget())
    end_date = forms.DateField(widget=admin.widgets.AdminDateWidget())

    class Meta:
        model = Driverwork
        fields = '__all__'
# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display=('name','driverid', 'password','isadmin')
class DriverworkAdmin(admin.ModelAdmin):
    list_display=('driverid',"corporatename","location","gatepassno","date","name","pickupplace","dropplace","vehicleno","imgbb_url",'update','display_image_preview')
    search_fields=["date",'corporatename','driverid','driverid']
    list_filter = [('date',DateRangeFilter)]
    def display_image_preview(self, obj):
        # Return the formatted HTML for displaying the image preview
        return format_html('<img src="{}" width="50" height="50" />', obj.imgbb_url)
    display_image_preview.short_description = 'Image Preview' 
    def download_data_in_date_range(self, request, queryset):
        form = DateRangeForm(request.POST or None)

        if form.is_valid():
            # Get the selected date range
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            # Filter the queryset based on the date range
            queryset = queryset.filter(date_field__range=(start_date, end_date))

            # Create a CSV response with filtered data
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="data_in_date_range.csv"'

            # Write the CSV header
            csv_writer = csv.writer(response)
            csv_writer.writerow(['Title', 'Date Field'])  # Adjust these headers based on your actual fields

            # Write the filtered data to the CSV
            for obj in queryset:
                csv_writer.writerow([obj.title, obj.date_field])  # Adjust this based on your actual fields

            return response

        context = {
            'queryset': queryset,
            'form': form,
            'title': 'Download data in date range',
            'action_checkbox_name': admin.helpers.ACTION_CHECKBOX_NAME,
        }
        return render(request, 'admin/download_data_in_date_range.html', context)

    download_data_in_date_range.short_description = "Download data in date range"
    actions = [export_to_excel,"download_data_in_date_range"]

    
class CorporateAdmin(admin.ModelAdmin):
    list_display=['name']
class PlacesAdmin(admin.ModelAdmin):
    list_display=['places']
admin.site.register(Users,UsersAdmin)
admin.site.register(Places,PlacesAdmin)
admin.site.register(Corporate,CorporateAdmin)
admin.site.register(Driverwork,DriverworkAdmin)