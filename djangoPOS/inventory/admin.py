from django.contrib import admin

# Register your models here.
from inventory.models import Items


class ItemsAdmin(admin.ModelAdmin):
    exclude = ['last_modified', 'ecommerce_last_modified']

admin.site.register(Items, ItemsAdmin)
