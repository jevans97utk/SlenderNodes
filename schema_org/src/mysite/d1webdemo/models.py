# standard library imports
import datetime

# 3rd party library imports
from django.db import models
from django.utils import timezone


# Create your models here.
class Site(models.Model):
    url = models.CharField(max_length=200)
    harvest_date = models.DateTimeField('date of last harvest')

    def __str__(self):
        return self.url

    def was_harvested_recently(self):
        return self.harvest_date >= timezone.now() - datetime.timedelta(days=1)


class Document(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    landing_page_url = models.CharField(max_length=200)
    last_modification_date = models.DateTimeField('date of last modification')
    json_ld = models.CharField(max_length=10000)
    metadata_url = models.CharField(max_length=200)

    def __str__(self):
        return self.landing_page_url

    def was_modified_recently(self):
        recent_time = timezone.now() - datetime.timedelta(days=1)
        return self.last_modification_date >= recent_time
