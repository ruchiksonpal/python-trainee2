# Generated by Django 3.0.4 on 2020-03-19 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0014_auto_20200319_0423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.TextField(unique=True),
        ),
    ]