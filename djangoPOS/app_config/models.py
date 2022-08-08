from base.models import AbstractBaseModel
from django.db import models

# Create your models here.
# from locations.models import Locations


class AppFiles(AbstractBaseModel):
    file_id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=255)
    file_data = models.TextField()
    timestamp = models.DateTimeField()
    expires = models.DateTimeField(blank=True, null=True)

    class Meta:
        
        db_table = 'pos_app_files'


class TaxClasses(AbstractBaseModel):
    order = models.IntegerField()
    # location = models.ForeignKey(Locations, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    ecommerce_tax_class_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        
        db_table = 'pos_tax_classes'


class AppConfig(AbstractBaseModel):
    key = models.CharField(primary_key=True, max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        
        db_table = 'pos_app_config'
