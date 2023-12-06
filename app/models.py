from django.db import models
from .utils import *
import os
from zaid.settings import MEDIA_ROOT
# Create your models here.
class Users(models.Model):
    name=models.CharField(max_length=2080,default='Driver Name')
    driverid=models.CharField(max_length=2080)
    password=models.CharField(max_length=2080)
    isadmin=models.CharField(max_length=2080,default='No')

class Places(models.Model):
    places=models.CharField(max_length=2080)

class Driverwork(models.Model):
    driverid=models.CharField(max_length=2080)
    corporatename=models.CharField(max_length=2080)
    location=models.CharField(max_length=2080)
    gatepassno=models.CharField(max_length=2080)
    date=models.CharField(max_length=2080)
    name=models.CharField(max_length=2080)
    pickupplace=models.CharField(max_length=2080)
    dropplace=models.CharField(max_length=2080)
    vehicleno=models.CharField(max_length=2080)
    photo=models.ImageField(upload_to='photos/')
    imgbb_url = models.URLField(blank=True)
    update=models.BooleanField(default=True)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.photo:
            imgbb_url = upload_to_imgbb(self.photo)  # Use the function
            if imgbb_url:
                image_path = os.path.join(MEDIA_ROOT, self.photo.name)
                print(image_path)
                print(os.path.exists(image_path))
                self.imgbb_url = imgbb_url
                if os.path.exists(image_path):
                    print('yes')
                super().save(update_fields=['imgbb_url'])
    def delete(self, *args, **kwargs):
        # Get the path of the image file
        image_path = os.path.join(MEDIA_ROOT, self.photo.name)
        print(image_path)
        # Delete the image file from the filesystem
        if os.path.exists(image_path):
            print('yes')
            os.remove(image_path)

        super().delete(*args, **kwargs)
        

class Corporate(models.Model):
    name=models.CharField(max_length=2080)

class YourModel(models.Model):
    # Add your other fields here

    # Define a FileField to store PDF files
    pdf_file = models.FileField(upload_to='pdfs/')  # 'pdfs/' is the directory where PDFs will be stored

