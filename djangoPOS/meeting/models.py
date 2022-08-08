from base.models import AbstractBaseModel
from django.db import models


# Create your models here.

class NewModel(AbstractBaseModel):
    description = models.CharField(max_length=255, blank=True, null=True)
    line = models.IntegerField()
