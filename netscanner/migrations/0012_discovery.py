# Generated by Django 2.2.5 on 2019-10-17 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('netscanner', '0011_scanner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discovery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('enabled', models.BooleanField(verbose_name='enabled')),
                ('arguments', models.TextField(blank=True, verbose_name='arguments')),
                ('interval', models.PositiveIntegerField(verbose_name='scan interval')),
                ('last_scan', models.DateTimeField(blank=True, default=None, null=True, verbose_name='last scan')),
                ('scanner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='netscanner.Scanner', verbose_name='scanner')),
                ('subnetv4', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='netscanner.SubnetV4', verbose_name='subnet v4')),
            ],
            options={
                'verbose_name': 'Discovery',
                'verbose_name_plural': 'Discoveries',
                'db_table': 'netscanner_discovery',
                'ordering': ['name'],
            },
        ),
    ]
