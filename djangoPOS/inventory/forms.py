"""
Author: Elijah Kinyanjui
(c) Copyright by HugosLabs ltd

File: 
Description: 


"""
from ast import Div
from dataclasses import fields
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column, HTML, Button
from crispy_forms.bootstrap import InlineRadios, FormActions
from django import forms
from django.utils import timezone

from inventory.models import Items


class ItemsForm(forms.ModelForm):

    model = Items

    class Meta:
        model = Items

        # fields = [
        #     __all__
        # ]

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Row(
                Column('name'),
                Column('item_number'),
            ),
            Row(
                Column('category'),
                Column('tags'),
            ),
            Row(
                Column('supplier'),
                Column('manufacturer'),
            ),
            'description',
            Row(
                Column('cost_price'),
                Column('unit_price'),
            ),
            Row(
                Column('weight'),
                Column('weight_unit'),
                Column('length'),
            ),
            'default_quantity',
            Row(
                Column('item_inactive'),
                Column('is_service'),
                Column('disable_loyalty'),
            ),

            'loyalty_multiplier',
            FormActions(
                Submit('submit', 'Submit'),
                Button('cancel', 'Cancel', css_class='ml-5 btn btn-danger',
                       onclick="window.history.back()"),
            )
        )


class ItemsPricingForm(ItemsForm):
    start_date = forms.DateTimeField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'min': timezone.now().date()})
    )
    end_date = forms.DateTimeField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'min': timezone.now().date()})
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
