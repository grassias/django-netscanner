# Generated by Django 2.2.5 on 2019-10-17 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0012_custom_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminlistdisplay',
            name='model',
            field=models.CharField(choices=[('AdminListDisplayAdmin', 'AdminListDisplayAdmin'), ('AdminListDisplayLinkAdmin', 'AdminListDisplayLinkAdmin'), ('AdminListFilterAdmin', 'AdminListFilterAdmin'), ('BrandAdmin', 'BrandAdmin'), ('CompanyAdmin', 'CompanyAdmin'), ('CustomFieldAdmin', 'CustomFieldAdmin'), ('DeviceModelAdmin', 'DeviceModelAdmin'), ('DeviceTypeAdmin', 'DeviceTypeAdmin'), ('DomainAdmin', 'DomainAdmin'), ('DomainMainAdmin', 'DomainMainAdmin'), ('LocationAdmin', 'LocationAdmin'), ('OperatingSystemAdmin', 'OperatingSystemAdmin'), ('ScannerAdmin', 'ScannerAdmin'), ('SubnetV4Admin', 'SubnetV4Admin')], max_length=255, verbose_name='model'),
        ),
        migrations.AlterField(
            model_name='adminlistdisplaylink',
            name='model',
            field=models.CharField(choices=[('AdminListDisplayAdmin', 'AdminListDisplayAdmin'), ('AdminListDisplayLinkAdmin', 'AdminListDisplayLinkAdmin'), ('AdminListFilterAdmin', 'AdminListFilterAdmin'), ('BrandAdmin', 'BrandAdmin'), ('CompanyAdmin', 'CompanyAdmin'), ('CustomFieldAdmin', 'CustomFieldAdmin'), ('DeviceModelAdmin', 'DeviceModelAdmin'), ('DeviceTypeAdmin', 'DeviceTypeAdmin'), ('DomainAdmin', 'DomainAdmin'), ('DomainMainAdmin', 'DomainMainAdmin'), ('LocationAdmin', 'LocationAdmin'), ('OperatingSystemAdmin', 'OperatingSystemAdmin'), ('ScannerAdmin', 'ScannerAdmin'), ('SubnetV4Admin', 'SubnetV4Admin')], max_length=255, verbose_name='model'),
        ),
        migrations.AlterField(
            model_name='adminlistfilter',
            name='model',
            field=models.CharField(choices=[('AdminListDisplayAdmin', 'AdminListDisplayAdmin'), ('AdminListDisplayLinkAdmin', 'AdminListDisplayLinkAdmin'), ('AdminListFilterAdmin', 'AdminListFilterAdmin'), ('BrandAdmin', 'BrandAdmin'), ('CompanyAdmin', 'CompanyAdmin'), ('CustomFieldAdmin', 'CustomFieldAdmin'), ('DeviceModelAdmin', 'DeviceModelAdmin'), ('DeviceTypeAdmin', 'DeviceTypeAdmin'), ('DomainAdmin', 'DomainAdmin'), ('DomainMainAdmin', 'DomainMainAdmin'), ('LocationAdmin', 'LocationAdmin'), ('OperatingSystemAdmin', 'OperatingSystemAdmin'), ('ScannerAdmin', 'ScannerAdmin'), ('SubnetV4Admin', 'SubnetV4Admin')], max_length=255, verbose_name='model'),
        ),
    ]
