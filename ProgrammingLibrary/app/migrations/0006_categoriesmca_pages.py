# Generated by Django 4.2.1 on 2023-07-19 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_categoriesmca_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoriesmca',
            name='pages',
            field=models.URLField(default='SOME STRING', null=True),
        ),
    ]
