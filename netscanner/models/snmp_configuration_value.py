##
#     Project: Django NetScanner
# Description: A Django application to make network scans
#      Author: Fabio Castelli (Muflone) <muflone@muflone.com>
#   Copyright: 2019 Fabio Castelli
#     License: GPL-3+
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
##

from django.db import models
from django.utils.translation import pgettext_lazy

from utility.models import BaseModel, BaseModelAdmin


class SNMPConfigurationValue(BaseModel):
    snmp_configuration = models.ForeignKey('SNMPConfiguration',
                                           blank=False,
                                           on_delete=models.PROTECT,
                                           verbose_name=pgettext_lazy(
                                               'SNMPConfiguration',
                                               'configuration'))
    snmp_value = models.ForeignKey('SNMPValue',
                                   blank=False,
                                   on_delete=models.PROTECT,
                                   related_name='snmp_configuration_value'
                                                '_values',
                                   verbose_name=pgettext_lazy(
                                       'SNMPConfiguration',
                                       'value'))
    field = models.CharField(max_length=255,
                             blank=True,
                             verbose_name=pgettext_lazy(
                                 'SNMPConfigurationValue',
                                 'field'))
    text_values = models.TextField(blank=True,
                                   verbose_name=pgettext_lazy(
                                       'SNMPConfigurationValue',
                                       'JSON text values'))

    class Meta:
        # Define the database table
        db_table = 'netscanner_snmp_configuration_values'
        ordering = ['snmp_configuration', 'snmp_value']
        unique_together = (('snmp_configuration', 'snmp_value'))
        verbose_name = pgettext_lazy('SNMPConfiguration',
                                     'SNMP Configuration value')
        verbose_name_plural = pgettext_lazy('SNMPConfiguration',
                                            'SNMP Configuration values')

    def __str__(self):
        return '{CONFIGURATION} {VALUE}'.format(
            CONFIGURATION=self.snmp_configuration,
            VALUE=self.snmp_value)


class SNMPConfigurationValueAdmin(BaseModelAdmin):
    pass
