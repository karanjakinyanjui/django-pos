from django.shortcuts import render
from django.views.generic import UpdateView, CreateView
from django.views.generic.base import TemplateResponseMixin

from inventory.forms import ItemsForm, ItemsPricingForm
from inventory.models import Items


def home(request):
    return render(request, "home.html")


def items(request):
    return render(request, "inventory/item_list.html", {"items": Items.objects.all(), "currency": "$"})


class ItemFormView(TemplateResponseMixin):
    model = Items
    form_class = ItemsForm
    template_name = "inventory/item_form.html"
    success_url = "#"


class ItemUpdateView(ItemFormView, UpdateView):
    tabs = [
        {
            "label": "Item Info",
            "url": "update_item",
        },
        {
            "label": "Item Pricing",
            "url": "item_pricing",
        },
        {
            "label": "Item Variations",
            "url": "item_variations",
        },
        {
            "label": "Item Images",
            "url": "item_images",
        },
        {
            "label": "Item Locations",
            "url": "item_locations",
        }
    ]
    extra_context = {"tabs": tabs}


class ItemCreateView(ItemFormView, CreateView):
    pass


class ItemPricingView(ItemUpdateView):
    form_class = ItemsPricingForm
