# Generated by Django 2.2.5 on 2019-11-03 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oui', '0001_oui'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oui',
            name='address',
            field=models.CharField(blank=True, max_length=255, verbose_name='address'),
        ),
    ]
