from base.models import AbstractBaseModel
from django.db import models

from app_config.models import AppFiles, TaxClasses


class People(AbstractBaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    full_name = models.TextField()
    phone_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    comments = models.TextField()
    image = models.ForeignKey(AppFiles, models.DO_NOTHING, blank=True, null=True, related_name="person")
    person_id = models.AutoField(primary_key=True)
    create_date = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        
        db_table = 'pos_people'

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return self.name


class Suppliers(AbstractBaseModel):
    person = models.ForeignKey(People, models.DO_NOTHING)
    company_name = models.CharField(max_length=255)
    account_number = models.CharField(unique=True, max_length=255, blank=True, null=True)
    override_default_tax = models.IntegerField()
    balance = models.DecimalField(max_digits=23, decimal_places=2)
    tax_class = models.ForeignKey(TaxClasses, models.DO_NOTHING, blank=True, null=True)
    custom_field_1_value = models.CharField(max_length=255, blank=True, null=True)
    custom_field_2_value = models.CharField(max_length=255, blank=True, null=True)
    custom_field_3_value = models.CharField(max_length=255, blank=True, null=True)
    custom_field_4_value = models.CharField(max_length=255, blank=True, null=True)
    custom_field_5_value = models.CharField(max_length=255, blank=True, null=True)
    custom_field_6_value = models.CharField(max_length=255, blank=True, null=True)
    custom_field_7_value = models.CharField(max_length=255, blank=True, null=True)
    custom_field_8_value = models.CharField(max_length=255, blank=True, null=True)
    custom_field_9_value = models.CharField(max_length=255, blank=True, null=True)
    custom_field_10_value = models.CharField(max_length=255, blank=True, null=True)
    internal_notes = models.TextField(blank=True, null=True)
    default_term_id = models.BooleanField(default=False)

    class Meta:
        
        db_table = 'pos_suppliers'

    def __str__(self) -> str:
        return f"{self.company_name} - {self.person.name}"


class Manufacturers(AbstractBaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        
        db_table = 'pos_manufacturers'

    def __str__(self) -> str:
        return f"{self.name}"


class Employees(AbstractBaseModel):
    username = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    person = models.ForeignKey('People', models.DO_NOTHING)

    class Meta:
        
        db_table = 'pos_employees'


class Customers(AbstractBaseModel):
    person = models.ForeignKey('People', models.DO_NOTHING)
    account_number = models.CharField(unique=True, max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255)
    taxable = models.IntegerField()

    class Meta:
        
        db_table = 'pos_customers'
