# Generated by Django 4.2.11 on 2024-03-19 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weddingSite', '0014_alter_giftcart_guest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='giftcart',
            name='gift',
        ),
        migrations.RemoveField(
            model_name='giftcart',
            name='total',
        ),
        migrations.AddField(
            model_name='giftcart',
            name='gifts',
            field=models.ManyToManyField(related_name='gift_cart', to='weddingSite.gift'),
        ),
    ]