# Generated by Django 3.2.4 on 2021-07-05 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='product',
            new_name='prod',
        ),
    ]