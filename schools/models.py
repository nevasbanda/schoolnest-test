import geocoder
from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.

mapbox_access_token = 'pk.eyJ1IjoibmV2YXMiLCJhIjoiY2w3M2gxNHFhMDBkNDN3dGhmaDRmODFtZSJ9.X3kdmczFQzfx9Y9ENY0YCQ'


class Province(models.Model):
    province_name = models.CharField(max_length=200)

    def __str__(self):
        return self.province_name


class School(models.Model):
    school_logo = models.ImageField(null=False, blank=False)
    school_name = models.CharField(max_length=255, null=False, blank=False)
    country = models.CharField(max_length=200)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, default=True, null=False)
    district = models.CharField(max_length=100)
    suburb = models.CharField(max_length=100)
    school_lat = models.FloatField(blank=True, null=True)
    school_lng = models.FloatField(blank=True, null=True)
    school_motto = models.CharField(max_length=255, null=False, blank=False)
    school_about = RichTextField(blank=True, null=True)
    school_address = models.TextField()
    school_contact = models.CharField(max_length=255,null=False, blank=False)
    school_email = models.EmailField(max_length=255)
    school_website = models.CharField(max_length=255)
    school_vacancy = RichTextField(blank=True, null=True)
    school_academics = RichTextField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.school_name, key=mapbox_access_token)
        g = g.latlng
        return super(School, self).save(*args, **kwargs)

    def __str__(self):
        return self.school_name
