# Generated by Django 4.0.5 on 2022-08-04 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('full_name', models.TextField()),
                ('phone_number', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('address_1', models.CharField(max_length=255)),
                ('address_2', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zip', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('comments', models.TextField()),
                ('person_id', models.AutoField(primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('last_modified', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'phppos_people',
                'managed': False,
            },
        ),
    ]