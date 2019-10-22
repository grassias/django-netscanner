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

from .models.location import Location
from .models.snmp_configuration import SNMPConfiguration
from .models.subnet_v4 import SubnetV4


class ConfirmActionForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)


class ChangeLocationForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    location = forms.ModelChoiceField(
        queryset=Location.objects,
        required=False,
        label=pgettext_lazy('Host',
                            'Location'))


class ChangeSNMPConfigurationForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    snmp_configuration = forms.ModelChoiceField(
        queryset=SNMPConfiguration.objects,
        required=False,
        label=pgettext_lazy('Host',
                            'SNMP configuration'))


class ChangeSubnetV4Form(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    subnetv4 = forms.ModelChoiceField(
        queryset=SubnetV4.objects,
        required=False,
        label=pgettext_lazy('Host',
                            'Subnet v4'))
