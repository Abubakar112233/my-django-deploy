# Generated by Django 4.0.1 on 2023-01-13 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_producttag'),
    ]

    operations = [
        migrations.AddField(
            model_name='productattribute',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
