# Generated by Django 3.2.4 on 2021-06-27 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210623_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
