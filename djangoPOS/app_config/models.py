from django.db import models

# Create your models here.
# from locations.models import Locations


class AppFiles(models.Model):
    file_id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=255)
    file_data = models.TextField()
    timestamp = models.DateTimeField()
    expires = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_app_files'


class TaxClasses(models.Model):
    order = models.IntegerField()
    # location = models.ForeignKey(Locations, models.DO_NOTHING, blank=True, null=True)
    deleted = models.IntegerField()
    name = models.CharField(max_length=255)
    ecommerce_tax_class_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_tax_classes'


class AppConfig(models.Model):
    key = models.CharField(primary_key=True, max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'pos_app_config'
