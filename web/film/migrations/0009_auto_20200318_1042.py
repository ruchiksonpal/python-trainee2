# Generated by Django 3.0.4 on 2020-03-18 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0008_actor'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmactor',
            name='actor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='actor_film', to='film.Actor', verbose_name='Actor'),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.TextField(max_length=200, unique=True),
        ),
    ]
