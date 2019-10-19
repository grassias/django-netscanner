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

import argparse

from django.utils import timezone

from netscanner.management.management_base_command import ManagementBaseCommand
from netscanner.models import Discovery, Domain, Host
from netscanner.tools.hostname import Hostname


class Command(ManagementBaseCommand):
    help = 'Discover network hostnames'

    def __init__(self):
        super().__init__()
        self.scanner_tool = 'hostname'

    def add_arguments(self, parser: argparse.ArgumentParser):
        super().add_arguments(parser)
        parser.add_argument('--workers',
                            action='store',
                            type=int,
                            default=10)

    def instance_scanner_tool(self,
                              options: dict):
        """
        Instance the scanner tool using the discovery options
        :param options: dictionary containing the options
        :return:
        """
        return Hostname()

    def process_results(self,
                        discovery: Discovery,
                        results: list) -> None:
        """
        Process the results list
        :param results: list of results to process
        :return: None
        """
        for item in results:
            if (item and item[1] and
                    item[1]['hostname'] and
                    item[1]['hostname'] != item[0]):
                # Update hostname and domain name
                address = item[0]
                if '.' in item[1]['hostname']:
                    # Hostname + domain name
                    hostname, domain_name = item[1]['hostname'].split('.', 1)
                    # Search for domain
                    domains = Domain.objects.filter(
                        domain__name=domain_name,
                        name='')
                    domain = domains[0] if domains else None
                    # If no domain is found, search for sub-domain
                    if not domain and '.' in domain_name:
                        domain_name, parent = domain_name.split('.', 1)
                        domains = Domain.objects.filter(
                            domain__name=parent,
                            name=domain_name)
                        domain = domains[0] if domains else None
                else:
                    # No domain, only hostname
                    hostname = item[1]['hostname']
                    domain = None
                self.print('%s %s' % (item[0], item[1]))
                hosts = Host.objects.filter(address=address)
                if hosts:
                    # Update existing hosts
                    for host in hosts:
                        # Update only if not excluded from discovery
                        if not host.no_discovery:
                            host.hostname = hostname
                            if domain:
                                host.domain = domain
                            host.last_seen = timezone.now()
                            host.save()
                else:
                    # Insert new host
                    host = Host.objects.create()
                    host.name = address
                    host.subnetv4 = discovery.subnetv4
                    host.hostname = hostname
                    if domain:
                        host.domain = domain
                    host.last_seen = timezone.now()
                    host.save()
