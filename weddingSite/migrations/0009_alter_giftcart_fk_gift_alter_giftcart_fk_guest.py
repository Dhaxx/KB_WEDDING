# Generated by Django 5.0.3 on 2024-03-18 17:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weddingSite', '0008_giftcart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giftcart',
            name='fk_gift',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='weddingSite.gift'),
        ),
        migrations.AlterField(
            model_name='giftcart',
            name='fk_guest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='weddingSite.guest'),
        ),
    ]
