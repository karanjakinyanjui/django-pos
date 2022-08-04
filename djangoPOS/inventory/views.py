from django.shortcuts import render


# Create your views here.
from inventory.models import Items


def home(request):
    return render(request, "home.html")


def items(request):
    return render(request, "inventory/item_list.html", {"items": Items.objects.all(), "currency": "$"})