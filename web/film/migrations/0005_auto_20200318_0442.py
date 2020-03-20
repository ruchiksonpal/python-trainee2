# Generated by Django 3.0.4 on 2020-03-18 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0004_auto_20200317_1104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='type',
            new_name='role',
        ),
        migrations.AlterField(
            model_name='actor',
            name='last_update',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Last update date'),
        ),
    ]
