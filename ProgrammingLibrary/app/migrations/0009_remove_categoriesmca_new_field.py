# Generated by Django 4.2.1 on 2023-07-19 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_categoriesmca_pages_categoriesmca_new_field_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoriesmca',
            name='new_field',
        ),
    ]
