# Generated by Django 4.0.4 on 2022-06-01 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_habr_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habr',
            name='category',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.PROTECT, to='mainapp.category', verbose_name='Категория'),
        ),
    ]