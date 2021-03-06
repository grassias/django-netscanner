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

from django.contrib import admin

from .models.brand import Brand, BrandAdmin
from .models.company import Company, CompanyAdmin
from .models.custom_field import CustomField, CustomFieldAdmin
from .models.device_model import DeviceModel, DeviceModelAdmin
from .models.device_type import DeviceType, DeviceTypeAdmin
from .models.discovery import Discovery, DiscoveryAdmin
from .models.discovery_result import DiscoveryResult, DiscoveryResultAdmin
from .models.domain import Domain, DomainAdmin
from .models.domain_main import DomainMain, DomainMainAdmin
from .models.host import Host, HostAdmin, HostProxy, HostProxyAdmin
from .models.host_custom_field import HostCustomField, HostCustomFieldAdmin
from .models.location import Location, LocationAdmin
from .models.operating_system import OperatingSystem, OperatingSystemAdmin
from .models.scanner import Scanner, ScannerAdmin
from .models.snmp_configuration import (SNMPConfiguration,
                                        SNMPConfigurationAdmin)
from .models.snmp_configuration_value import (SNMPConfigurationValue,
                                              SNMPConfigurationValueAdmin)
from .models.snmp_section import SNMPSection, SNMPSectionAdmin
from .models.snmp_value import SNMPValue, SNMPValueAdmin
from .models.snmp_version import SNMPVersion, SNMPVersionAdmin
from .models.subnet_v4 import SubnetV4, SubnetV4Admin


admin.site.register(Brand, BrandAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(CustomField, CustomFieldAdmin)
admin.site.register(DeviceModel, DeviceModelAdmin)
admin.site.register(DeviceType, DeviceTypeAdmin)
admin.site.register(Discovery, DiscoveryAdmin)
admin.site.register(DiscoveryResult, DiscoveryResultAdmin)
admin.site.register(Domain, DomainAdmin)
admin.site.register(DomainMain, DomainMainAdmin)
admin.site.register(Host, HostAdmin)
admin.site.register(HostProxy, HostProxyAdmin)
admin.site.register(HostCustomField, HostCustomFieldAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(OperatingSystem, OperatingSystemAdmin)
admin.site.register(Scanner, ScannerAdmin)
admin.site.register(SNMPConfiguration, SNMPConfigurationAdmin)
admin.site.register(SNMPConfigurationValue, SNMPConfigurationValueAdmin)
admin.site.register(SNMPSection, SNMPSectionAdmin)
admin.site.register(SNMPValue, SNMPValueAdmin)
admin.site.register(SNMPVersion, SNMPVersionAdmin)
admin.site.register(SubnetV4, SubnetV4Admin)
