# Generated by Django 5.0.3 on 2024-03-16 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weddingSite', '0004_remove_table_guests_guest_fk_table_table_fk_guests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='fk_guests',
            field=models.ManyToManyField(limit_choices_to={'guests__isnull': True}, related_name='guest_tables', to='weddingSite.guest'),
        ),
    ]
