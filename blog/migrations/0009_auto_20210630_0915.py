# Generated by Django 3.2.4 on 2021-06-30 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20210630_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='response',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
