# Generated by Django 4.2.3 on 2023-07-30 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0002_alter_booking_options_alter_menu_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(),
        ),
    ]
