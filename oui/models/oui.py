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

from utility.misc.admin_text_input_filter import AdminTextInputFilter
from utility.models import BaseModel, BaseModelAdmin


class Oui(BaseModel):
    prefix = models.CharField(max_length=255,
                              unique=True,
                              verbose_name=pgettext_lazy('Oui',
                                                         'prefix'))
    organization = models.CharField(max_length=255,
                                    verbose_name=pgettext_lazy('Oui',
                                                               'organization'))
    address = models.CharField(max_length=255,
                               blank=True,
                               verbose_name=pgettext_lazy('Oui',
                                                          'address'))

    class Meta:
        # Define the database table
        db_table = 'oui_oui'
        ordering = ['prefix']
        verbose_name = pgettext_lazy('Oui', 'Vendor OUI')
        verbose_name_plural = pgettext_lazy('Oui', 'Vendor OUIs')

    def __str__(self):
        return '{PREFIX}'.format(PREFIX=self.prefix)


class OuiAdmin(BaseModelAdmin):
    pass


class OuiAdminPrefixInputFilter(AdminTextInputFilter):
    """
    Filter OUI by prefix
    """
    parameter_name = 'prefix'
    title = pgettext_lazy('Oui', 'prefix')

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(prefix__startswith=self.value())


class OuiAdminOrganizationInputFilter(AdminTextInputFilter):
    """
    Filter OUI by organization
    """
    parameter_name = 'organization'
    title = pgettext_lazy('Oui', 'organization')

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(organization__icontains=self.value())
