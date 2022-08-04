from django.db import models

# Create your models here.
from app_config import models as config


class Locations(models.Model):
    location_id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    company = models.TextField(blank=True, null=True)
    website = models.TextField(blank=True, null=True)
    company_logo = models.ForeignKey(config.AppFiles, models.DO_NOTHING, db_column='company_logo', blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    fax = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    cc_email = models.TextField(blank=True, null=True)
    bcc_email = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)
    return_policy = models.TextField(blank=True, null=True)
    receive_stock_alert = models.TextField(blank=True, null=True)
    stock_alert_email = models.TextField(blank=True, null=True)
    timezone = models.TextField(blank=True, null=True)
    mailchimp_api_key = models.TextField(blank=True, null=True)
    enable_credit_card_processing = models.TextField(blank=True, null=True)
    credit_card_processor = models.TextField(blank=True, null=True)
    hosted_checkout_merchant_id = models.TextField(blank=True, null=True)
    hosted_checkout_merchant_password = models.TextField(blank=True, null=True)
    emv_merchant_id = models.TextField(blank=True, null=True)
    net_e_pay_server = models.TextField(blank=True, null=True)
    listener_port = models.TextField(blank=True, null=True)
    com_port = models.TextField(blank=True, null=True)
    stripe_public = models.TextField(blank=True, null=True)
    stripe_private = models.TextField(blank=True, null=True)
    stripe_currency_code = models.TextField(blank=True, null=True)
    braintree_merchant_id = models.TextField(blank=True, null=True)
    braintree_public_key = models.TextField(blank=True, null=True)
    braintree_private_key = models.TextField(blank=True, null=True)
    default_tax_1_rate = models.TextField(blank=True, null=True)
    default_tax_1_name = models.TextField(blank=True, null=True)
    default_tax_2_rate = models.TextField(blank=True, null=True)
    default_tax_2_name = models.TextField(blank=True, null=True)
    default_tax_2_cumulative = models.TextField(blank=True, null=True)
    default_tax_3_rate = models.TextField(blank=True, null=True)
    default_tax_3_name = models.TextField(blank=True, null=True)
    default_tax_4_rate = models.TextField(blank=True, null=True)
    default_tax_4_name = models.TextField(blank=True, null=True)
    default_tax_5_rate = models.TextField(blank=True, null=True)
    default_tax_5_name = models.TextField(blank=True, null=True)
    deleted = models.BooleanField(default=False)
    secure_device_override_emv = models.CharField(max_length=255)
    secure_device_override_non_emv = models.CharField(max_length=255)
    tax_class = models.ForeignKey(config.TaxClasses, models.DO_NOTHING, blank=True, null=True)
    ebt_integrated = models.IntegerField()
    integrated_gift_cards = models.IntegerField()
    square_currency_code = models.CharField(max_length=255)
    square_location_id = models.CharField(max_length=255)
    square_currency_multiplier = models.CharField(max_length=255)
    email_sales_email = models.CharField(max_length=255, blank=True, null=True)
    email_receivings_email = models.CharField(max_length=255, blank=True, null=True)
    stock_alerts_just_order_level = models.BooleanField(default=False)
    platformly_api_key = models.TextField(blank=True, null=True)
    platformly_project_id = models.TextField(blank=True, null=True)
    tax_id = models.CharField(max_length=255)
    disable_markup_markdown = models.TextField(blank=True, null=True)
    card_connect_mid = models.CharField(max_length=255, blank=True, null=True)
    card_connect_rest_username = models.CharField(max_length=255, blank=True, null=True)
    card_connect_rest_password = models.CharField(max_length=255, blank=True, null=True)
    default_mailchimp_lists = models.CharField(max_length=255)
    twilio_sid = models.CharField(max_length=255, blank=True, null=True)
    twilio_token = models.CharField(max_length=255, blank=True, null=True)
    twilio_sms_from = models.CharField(max_length=255, blank=True, null=True)
    auto_reports_email = models.CharField(max_length=255)
    auto_reports_email_time = models.TimeField(blank=True, null=True)
    auto_reports_day = models.CharField(max_length=255)
    disable_confirmation_option_for_emv_credit_card = models.IntegerField()
    blockchyp_api_key = models.CharField(max_length=255, blank=True, null=True)
    blockchyp_bearer_token = models.CharField(max_length=255, blank=True, null=True)
    blockchyp_signing_key = models.CharField(max_length=255, blank=True, null=True)
    blockchyp_test_mode = models.CharField(max_length=255, blank=True, null=True)
    sidekick_api_key = models.TextField(blank=True, null=True)
    sidekick_auto_review = models.BooleanField(default=False)
    coreclear_merchant_id = models.CharField(max_length=255, blank=True, null=True)
    additional_appointment_note = models.TextField(blank=True, null=True)
    send_sms_via_whatsapp = models.IntegerField()
    blockchyp_terms_and_conditions = models.TextField()
    blockchyp_work_order_pre_auth = models.TextField()
    blockchyp_work_order_post_auth = models.TextField()

    class Meta:
        managed = False
        db_table = 'phppos_locations'
