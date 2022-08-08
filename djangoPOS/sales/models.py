from base.models import AbstractBaseModel
from django.db import models

# Create your models here.
from inventory.models import ItemKits, Items
from people.models import Employees, Customers


class Sales(AbstractBaseModel):
    sale_time = models.DateTimeField()
    customer = models.ForeignKey(Customers, models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey(Employees, models.DO_NOTHING)
    comment = models.TextField()
    show_comment_on_receipt = models.IntegerField()
    sale_id = models.AutoField(primary_key=True)
    payment_type = models.CharField(max_length=255, blank=True, null=True)
    cc_ref_no = models.CharField(max_length=255)
    suspended = models.IntegerField()

    class Meta:
        
        db_table = 'pos_sales'


class SalesItemKits(AbstractBaseModel):
    sale = models.OneToOneField(Sales, models.DO_NOTHING, primary_key=True)
    item_kit = models.ForeignKey(ItemKits, models.DO_NOTHING)
    description = models.CharField(max_length=255, blank=True, null=True)
    line = models.IntegerField()
    quantity_purchased = models.DecimalField(max_digits=15, decimal_places=2)
    item_kit_cost_price = models.DecimalField(max_digits=15, decimal_places=2)
    item_kit_unit_price = models.DecimalField(max_digits=15, decimal_places=2)
    discount_percent = models.IntegerField()

    class Meta:
        
        db_table = 'pos_sales_item_kits'
        unique_together = (('sale', 'item_kit', 'line'),)


class SalesItemKitsTaxes(AbstractBaseModel):
    sale = models.OneToOneField(SalesItemKits, models.DO_NOTHING, primary_key=True)
    item_kit = models.ForeignKey(ItemKits, models.DO_NOTHING)
    line = models.IntegerField()
    name = models.CharField(max_length=255)
    percent = models.DecimalField(max_digits=15, decimal_places=3)
    cumulative = models.IntegerField()

    class Meta:
        
        db_table = 'pos_sales_item_kits_taxes'
        unique_together = (('sale', 'item_kit', 'line', 'name', 'percent'),)


class SalesItems(AbstractBaseModel):
    sale = models.OneToOneField(Sales, models.DO_NOTHING, primary_key=True)
    item = models.ForeignKey(Items, models.DO_NOTHING)
    description = models.CharField(max_length=255, blank=True, null=True)
    serialnumber = models.CharField(max_length=255, blank=True, null=True)
    line = models.IntegerField()
    quantity_purchased = models.DecimalField(max_digits=15, decimal_places=2)
    item_cost_price = models.DecimalField(max_digits=15, decimal_places=2)
    item_unit_price = models.DecimalField(max_digits=15, decimal_places=2)
    discount_percent = models.IntegerField()

    class Meta:
        
        db_table = 'pos_sales_items'
        unique_together = (('sale', 'item', 'line'),)


class SalesItemsTaxes(AbstractBaseModel):
    sale = models.OneToOneField(SalesItems, models.DO_NOTHING, primary_key=True)
    item = models.ForeignKey(Items, models.DO_NOTHING)
    line = models.IntegerField()
    name = models.CharField(max_length=255)
    percent = models.DecimalField(max_digits=15, decimal_places=3)
    cumulative = models.IntegerField()

    class Meta:
        
        db_table = 'pos_sales_items_taxes'
        unique_together = (('sale', 'item', 'line', 'name', 'percent'),)


class SalesPayments(AbstractBaseModel):
    sale = models.OneToOneField(Sales, models.DO_NOTHING, primary_key=True)
    payment_type = models.CharField(max_length=255)
    payment_amount = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        
        db_table = 'pos_sales_payments'
        unique_together = (('sale', 'payment_type'),)


class Giftcards(AbstractBaseModel):
    giftcard_id = models.AutoField(primary_key=True)
    giftcard_number = models.CharField(unique=True, max_length=255)
    value = models.DecimalField(max_digits=15, decimal_places=2)
    customer = models.ForeignKey(Customers, models.DO_NOTHING, blank=True, null=True)
    
    class Meta:
        
        db_table = 'pos_giftcards'
