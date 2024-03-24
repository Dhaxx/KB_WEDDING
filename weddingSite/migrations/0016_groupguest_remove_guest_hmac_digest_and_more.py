# Generated by Django 5.0.3 on 2024-03-24 05:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weddingSite', '0015_remove_giftcart_gift_remove_giftcart_total_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupGuest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('token', models.CharField(max_length=100, unique=True)),
                ('hmac_digest', models.CharField(max_length=64)),
            ],
        ),
        migrations.RemoveField(
            model_name='guest',
            name='hmac_digest',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='token',
        ),
        migrations.AddField(
            model_name='guest',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='weddingSite.groupguest'),
        ),
    ]
