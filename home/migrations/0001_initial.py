# Generated by Django 3.2.4 on 2021-06-22 09:52

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255, null=True)),
                ('company', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('menu_icon', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('facebook', models.CharField(blank=True, max_length=50)),
                ('instagram', models.CharField(blank=True, max_length=50)),
                ('twitter', models.CharField(blank=True, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('about', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('contact', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10)),
            ],
        ),
    ]
