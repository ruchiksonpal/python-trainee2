# Generated by Django 3.0.4 on 2020-03-18 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0005_auto_20200318_0442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='last_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Last update date'),
        ),
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='address',
            name='postal_code',
            field=models.IntegerField(),
        ),
    ]