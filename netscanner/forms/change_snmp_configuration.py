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

from django import forms
from django.utils.translation import pgettext_lazy

from ..models.snmp_configuration import SNMPConfiguration

from utility.misc import ChangeFieldAction


class ChangeSNMPConfigurationForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    changed_data = forms.ModelChoiceField(
        queryset=SNMPConfiguration.objects,
        required=False,
        label=pgettext_lazy('Host',
                            'SNMP configuration'))


change_field_snmp_config_action = ChangeFieldAction(
    item='SNMP Configuration',
    field_name='snmp_configuration',
    title=pgettext_lazy('Host', 'Change SNMP Configuration'),
    question=pgettext_lazy('Host',
                           'Confirm you want to change the '
                           'SNMP configuration for the selected hosts?'),
    form=ChangeSNMPConfigurationForm)
