# Generated by Django 3.2.4 on 2021-07-14 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_rename_product_review_prod'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]
