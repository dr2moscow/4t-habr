# Generated by Django 4.0.4 on 2022-05-23 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habr',
            name='habr_view',
            field=models.IntegerField(default=1, verbose_name='просмотров'),
        ),
    ]
