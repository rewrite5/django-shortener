# Generated by Django 5.0.6 on 2024-05-24 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlshortener',
            name='original_url',
            field=models.URLField(max_length=2048),
        ),
    ]
