from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import UpdateView

from inventory.forms import ItemsForm
from inventory.models import Items


def home(request):
    return render(request, "home.html")


def items(request):
    return render(request, "inventory/item_list.html", {"items": Items.objects.all(), "currency": "$"})


class UpdateItemView(UpdateView):
    model = Items
    form_class = ItemsForm
    template_name = "inventory/item_form.html"
    success_url = "/items"

