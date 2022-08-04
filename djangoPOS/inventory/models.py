"""
Author: Elijah Kinyanjui
(c) Copyright by HugosLabs ltd

File:
Description:


"""
from uuid import uuid4

from django.db import models

from app_config.models import AppFiles, TaxClasses
from people.models import Suppliers, Manufacturers, Employees


def uuid():
	return uuid4()


class Categories(models.Model):
	ecommerce_category_id = models.CharField(max_length=255, blank=True, null=True)
	last_modified = models.DateTimeField()
	deleted = models.IntegerField()
	hide_from_grid = models.IntegerField()
	parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
	name = models.CharField(max_length=255)
	image = models.ForeignKey(AppFiles, models.DO_NOTHING, blank=True, null=True)
	color = models.TextField(blank=True, null=True)
	system_category = models.BooleanField(default=False)
	exclude_from_e_commerce = models.IntegerField()
	category_info_popup = models.TextField(blank=True, null=True)

	def __str__(self) -> str:
		return self.name

	class Meta:
		managed = False
		db_table = 'phppos_categories'


class Items(models.Model):
	name = models.CharField(max_length=255)
	category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
	supplier = models.ForeignKey(Suppliers, models.DO_NOTHING, blank=True, null=True)
	manufacturer = models.ForeignKey(Manufacturers, models.DO_NOTHING, blank=True, null=True)
	item_number = models.CharField(verbose_name="UPC/EAN/ISBN/SKU", unique=True, max_length=255, blank=True, null=True)
	product_id = models.CharField(unique=True, max_length=255, blank=True, null=True)
	ecommerce_product_id = models.CharField(max_length=255, blank=True, null=True)
	ecommerce_product_quantity = models.CharField(max_length=255, blank=True, null=True)
	description = models.TextField()
	size = models.CharField(max_length=255)
	tax_included = models.BooleanField(default=True)
	cost_price = models.DecimalField(max_digits=23, decimal_places=10)
	unit_price = models.DecimalField(max_digits=23, decimal_places=10)
	promo_price = models.DecimalField(max_digits=23, decimal_places=10, blank=True, null=True)
	start_date = models.DateField(blank=True, null=True)
	end_date = models.DateField(blank=True, null=True)
	reorder_level = models.DecimalField(max_digits=23, decimal_places=10, blank=True, null=True)
	expire_days = models.BooleanField(default=False)
	item_id = models.AutoField(primary_key=True)
	allow_alt_description = models.BooleanField(default=True)
	is_serialized = models.BooleanField(default=True)
	override_default_tax = models.BooleanField(default=True)
	is_ecommerce = models.BooleanField(default=True)
	is_service = models.BooleanField(default=True)
	is_ebt_item = models.BooleanField(default=True)
	commission_percent = models.DecimalField(max_digits=23, decimal_places=10, blank=True, null=True)
	commission_percent_type = models.CharField(max_length=255, blank=True, null=True)
	commission_fixed = models.DecimalField(max_digits=23, decimal_places=10, blank=True, null=True)
	change_cost_price = models.BooleanField(default=True)
	disable_loyalty = models.BooleanField(default=True)
	deleted = models.BooleanField(default=True)
	last_modified = models.DateTimeField()
	ecommerce_last_modified = models.DateTimeField(blank=True, null=True)
	tax_class = models.ForeignKey(TaxClasses, models.DO_NOTHING, blank=True, null=True)
	replenish_level = models.DecimalField(max_digits=23, decimal_places=10, blank=True, null=True)
	system_item = models.BooleanField(default=True)
	max_discount_percent = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
	max_edit_price = models.DecimalField(max_digits=23, decimal_places=10, blank=True, null=True)
	min_edit_price = models.DecimalField(max_digits=23, decimal_places=10, blank=True, null=True)
	required_age = models.BooleanField(default=False)
	verify_age = models.BooleanField(default=False)
	weight = models.DecimalField(max_digits=23, decimal_places=10, blank=True, null=True)
	length = models.DecimalField(max_digits=23, decimal_places=10, blank=True, null=True)
	width = models.DecimalField(max_digits=23, decimal_places=10, blank=True, null=True)
	height = models.DecimalField(max_digits=23, decimal_places=10, blank=True, null=True)
	ecommerce_shipping_class_id = models.CharField(max_length=255, blank=True, null=True)
	long_description = models.TextField()
	allow_price_override_regardless_of_permissions = models.BooleanField(default=False)
	main_image = models.ForeignKey('ItemImages', models.DO_NOTHING, blank=True, null=True)
	only_integer = models.BooleanField(default=True)
	is_series_package = models.BooleanField(default=True)
	series_quantity = models.BooleanField(default=False)
	series_days_to_use_within = models.BooleanField(default=False)
	is_barcoded = models.BooleanField(default=True)
	default_quantity = models.DecimalField(max_digits=23, decimal_places=10, blank=True, null=True)
	disable_from_price_rules = models.BooleanField(default=False)
	last_edited = models.DateTimeField(blank=True, null=True)
	info_popup = models.TextField(blank=True, null=True)
	item_inactive = models.BooleanField(default=False)
	barcode_name = models.CharField(max_length=255)
	tags = models.CharField(max_length=255, blank=True, null=True)
	is_favorite = models.BooleanField(default=False)
	loyalty_multiplier = models.DecimalField(max_digits=23, decimal_places=10, blank=True, null=True)
	ecommerce_inventory_item_id = models.CharField(max_length=255, blank=True, null=True)
	weight_unit = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return self.name

	class Meta:
		managed = False
		db_table = 'phppos_items'
		verbose_name_plural = 'Items'
		verbose_name = 'Item'


class ItemVariations(models.Model):
	ecommerce_variation_id = models.CharField(max_length=255, blank=True, null=True)
	ecommerce_variation_quantity = models.CharField(max_length=255, blank=True, null=True)
	deleted = models.IntegerField()
	item = models.ForeignKey(Items, models.DO_NOTHING)
	reorder_level = models.DecimalField(max_digits=23, decimal_places=10, blank=True, null=True)
	replenish_level = models.DecimalField(max_digits=23, decimal_places=10, blank=True, null=True)
	name = models.CharField(max_length=255, blank=True, null=True)
	item_number = models.CharField(unique=True, max_length=255, blank=True, null=True)
	unit_price = models.DecimalField(max_digits=23, decimal_places=10, blank=True, null=True)
	cost_price = models.DecimalField(max_digits=23, decimal_places=10, blank=True, null=True)
	promo_price = models.DecimalField(max_digits=23, decimal_places=10, blank=True, null=True)
	start_date = models.DateField(blank=True, null=True)
	end_date = models.DateField(blank=True, null=True)
	last_modified = models.DateTimeField()
	ecommerce_last_modified = models.DateTimeField(blank=True, null=True)
	is_ecommerce = models.IntegerField()
	ecommerce_inventory_item_id = models.CharField(max_length=255, blank=True, null=True)
	supplier = models.ForeignKey(Suppliers, models.DO_NOTHING, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'phppos_item_variations'


class ItemImages(models.Model):
	title = models.CharField(max_length=255)
	alt_text = models.CharField(max_length=255)
	item = models.ForeignKey(Items, models.DO_NOTHING, blank=True, null=True)
	item_variation = models.ForeignKey(ItemVariations, models.DO_NOTHING, blank=True, null=True)
	ecommerce_image_id = models.CharField(max_length=255, blank=True, null=True)
	image = models.ForeignKey(AppFiles, models.DO_NOTHING, blank=True, null=True)

	def __str__(self) -> str:
		return self.title or self.image.file_name

	class Meta:
		managed = False
		db_table = 'phppos_item_images'


class Inventory(models.Model):
	trans_id = models.AutoField(primary_key=True)
	trans_items = models.ForeignKey(Items, models.DO_NOTHING, db_column='trans_items')
	trans_user = models.ForeignKey(Employees, models.DO_NOTHING, db_column='trans_user')
	trans_date = models.DateTimeField()
	trans_comment = models.TextField()
	trans_inventory = models.DecimalField(max_digits=15, decimal_places=2)

	class Meta:
		managed = False
		db_table = 'phppos_inventory'


class ItemKitItems(models.Model):
	item_kit = models.OneToOneField('ItemKits', models.DO_NOTHING, primary_key=True)
	item = models.ForeignKey(Items, models.DO_NOTHING)
	quantity = models.DecimalField(max_digits=15, decimal_places=2)

	class Meta:
		managed = False
		db_table = 'phppos_item_kit_items'
		unique_together = (('item_kit', 'item', 'quantity'),)


class ItemKits(models.Model):
	item_kit_id = models.AutoField(primary_key=True)
	item_kit_number = models.CharField(unique=True, max_length=255, blank=True, null=True)
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	category = models.CharField(max_length=255)
	unit_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
	cost_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
	deleted = models.IntegerField()

	class Meta:
		managed = False
		db_table = 'phppos_item_kits'


class ItemKitsTaxes(models.Model):
	item_kit = models.OneToOneField(ItemKits, models.DO_NOTHING, primary_key=True)
	name = models.CharField(max_length=255)
	percent = models.DecimalField(max_digits=15, decimal_places=3)
	cumulative = models.IntegerField()

	class Meta:
		managed = False
		db_table = 'phppos_item_kits_taxes'
		unique_together = (('item_kit', 'name', 'percent'),)


class ItemsTaxes(models.Model):
	item = models.OneToOneField(Items, models.DO_NOTHING, primary_key=True)
	name = models.CharField(max_length=255)
	percent = models.DecimalField(max_digits=15, decimal_places=3)
	cumulative = models.IntegerField()

	class Meta:
		managed = False
		db_table = 'phppos_items_taxes'
		unique_together = (('item', 'name', 'percent'),)


class Receivings(models.Model):
	receiving_time = models.DateTimeField()
	supplier = models.ForeignKey(Suppliers, models.DO_NOTHING, blank=True, null=True)
	employee = models.ForeignKey(Employees, models.DO_NOTHING)
	comment = models.TextField()
	receiving_id = models.AutoField(primary_key=True)
	payment_type = models.CharField(max_length=255, blank=True, null=True)
	deleted = models.IntegerField()

	class Meta:
		managed = False
		db_table = 'phppos_receivings'


class ReceivingsItems(models.Model):
	receiving = models.OneToOneField(Receivings, models.DO_NOTHING, primary_key=True)
	item = models.ForeignKey(Items, models.DO_NOTHING)
	description = models.CharField(max_length=255, blank=True, null=True)
	serialnumber = models.CharField(max_length=255, blank=True, null=True)
	line = models.IntegerField()
	quantity_purchased = models.IntegerField()
	item_cost_price = models.DecimalField(max_digits=15, decimal_places=2)
	item_unit_price = models.DecimalField(max_digits=15, decimal_places=2)
	discount_percent = models.IntegerField()

	class Meta:
		managed = False
		db_table = 'phppos_receivings_items'
		unique_together = (('receiving', 'item', 'line'),)
