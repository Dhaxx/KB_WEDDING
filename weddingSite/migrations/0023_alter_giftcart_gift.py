# Generated by Django 5.0.3 on 2024-07-16 19:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weddingSite', '0022_remove_giftcart_gifts_giftcart_gift'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giftcart',
            name='gift',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gift_cart', to='weddingSite.gift'),
        ),
    ]
