# Generated by Django 4.0.5 on 2022-08-05 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_items_long_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='size',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
