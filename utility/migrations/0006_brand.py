# Generated by Django 2.2.5 on 2019-10-15 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0005_subnet_v4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminlistdisplay',
            name='model',
            field=models.CharField(choices=[('AdminListDisplayAdmin', 'AdminListDisplayAdmin'), ('AdminListDisplayLinkAdmin', 'AdminListDisplayLinkAdmin'), ('AdminListFilterAdmin', 'AdminListFilterAdmin'), ('BrandAdmin', 'BrandAdmin'), ('CompanyAdmin', 'CompanyAdmin'), ('DeviceTypeAdmin', 'DeviceTypeAdmin'), ('SubnetV4Admin', 'SubnetV4Admin')], max_length=255, verbose_name='model'),
        ),
        migrations.AlterField(
            model_name='adminlistdisplaylink',
            name='model',
            field=models.CharField(choices=[('AdminListDisplayAdmin', 'AdminListDisplayAdmin'), ('AdminListDisplayLinkAdmin', 'AdminListDisplayLinkAdmin'), ('AdminListFilterAdmin', 'AdminListFilterAdmin'), ('BrandAdmin', 'BrandAdmin'), ('CompanyAdmin', 'CompanyAdmin'), ('DeviceTypeAdmin', 'DeviceTypeAdmin'), ('SubnetV4Admin', 'SubnetV4Admin')], max_length=255, verbose_name='model'),
        ),
        migrations.AlterField(
            model_name='adminlistfilter',
            name='model',
            field=models.CharField(choices=[('AdminListDisplayAdmin', 'AdminListDisplayAdmin'), ('AdminListDisplayLinkAdmin', 'AdminListDisplayLinkAdmin'), ('AdminListFilterAdmin', 'AdminListFilterAdmin'), ('BrandAdmin', 'BrandAdmin'), ('CompanyAdmin', 'CompanyAdmin'), ('DeviceTypeAdmin', 'DeviceTypeAdmin'), ('SubnetV4Admin', 'SubnetV4Admin')], max_length=255, verbose_name='model'),
        ),
    ]