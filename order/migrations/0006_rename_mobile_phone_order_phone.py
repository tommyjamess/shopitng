# Generated by Django 3.2.4 on 2021-06-28 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_order_company_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='mobile_phone',
            new_name='phone',
        ),
    ]