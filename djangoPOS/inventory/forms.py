"""
Author: Elijah Kinyanjui
(c) Copyright by HugosLabs ltd

File: 
Description: 


"""
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.utils import timezone

from inventory.models import Items


class ItemsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.add_input(Submit('submit', 'Submit'))

    model = Items

    class Meta:
        model = Items
        fields = [
            "name",
            "item_number",
            "category",
            "supplier",
            "tags",
            "manufacturer",
            "description",
            'cost_price',
            'unit_price',
            # "long_description",
            # "info_popup",
            "weight",
            "weight_unit",
            "length",
            "default_quantity",
            "item_inactive",
            # "is_barcoded",
            # "is_favorite",
            # "is_series_package",
            # "series_quantity",
            # "series_quantity",
            # "series_days_to_use_within",
            "is_service",
            # "allow_alt_description",
            # "is_serialized",
            "disable_loyalty",
            "loyalty_multiplier"
        ]


class ItemsPricingForm(ItemsForm):
    start_date = forms.DateTimeField(
        widget=forms.DateInput(attrs={'type': 'date', 'min': timezone.now().date()})
    )
    end_date = forms.DateTimeField(
        widget=forms.DateInput(attrs={'type': 'date', 'min': timezone.now().date()})
    )

    class Meta:
        model = Items
        fields = [
            "cost_price",
            "unit_price",
            "promo_price",
            "start_date",
            "end_date",
            "disable_from_price_rules",
            "allow_price_override_regardless_of_permissions",
            "tax_included",
            "only_integer",
            "change_cost_price",
            # "override_default_commission",
            # "commission_value",
            # "commission_percent_type",
            "override_default_tax",
            # "tax_class",
            # "tax_names_0",
            # "tax_names_1",
            # "tax_names_2",
            # "tax_names_3",
            # "tax_names_4"
        ]
