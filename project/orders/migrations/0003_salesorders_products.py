# Generated by Django 4.1.7 on 2023-02-20 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('orders', '0002_salesorders_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesorders',
            name='products',
            field=models.ManyToManyField(to='products.product'),
        ),
    ]
