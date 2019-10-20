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
import json
import multiprocessing

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from netscanner.models import Discovery
from netscanner.utils.consumers import Consumers


class ManagementBaseCommand(BaseCommand):
    def __init__(self):
        """
        Management base command for all management commands
        Use scanner_tool string to choose the desider scanner to use
        """
        BaseCommand.__init__(self)
        self.scanner_tool = None

    def add_arguments(self, parser: argparse.ArgumentParser) -> None:
        BaseCommand.add_arguments(self, parser)

    def handle(self, *args, **options) -> None:
        discoveries = Discovery.objects.filter(scanner__tool=self.scanner_tool,
                                               enabled=True)
        for discovery in discoveries:
            # Define options (Command line + Scanner + Discovery)
            discovery_options = {**options}
            # Add Scanner options
            if discovery.scanner.options:
                discovery_options.update(json.loads(discovery.scanner.options))
            # Add Discovery options
            if discovery.options:
                discovery_options.update(json.loads(discovery.options))
            # Exlude Django reserved options
            for reserved_options in ('verbosity', 'settings', 'pythonpath',
                                     'traceback', 'no_color', 'force_color'):
                if reserved_options in discovery_options:
                    del discovery_options[reserved_options]
            # Prepare addresses to discover
            tasks = multiprocessing.JoinableQueue()
            for address in discovery.subnetv4.get_ip_list():
                tasks.put(address)
            # Prepare consumers to execute the network discovery
            consumers = Consumers(tasks_queue=tasks)
            # Instance the scanner tool using the discovery options
            tool = self.instance_scanner_tool(discovery_options)
            if tool:
                consumers.execute(runners=discovery_options['workers'],
                                  action=tool.execute)
                # Process the results in a single operation on the DB side
                with transaction.atomic():
                    self.process_results(discovery=discovery,
                                         options=options,
                                         results=consumers.results_as_list())
                    # Update last scan discovery
                    discovery.last_scan = timezone.now()
                    discovery.save()

    def instance_scanner_tool(self,
                              options: dict):
        """
        Instance the scanner tool using the discovery options
        :param options: dictionary containing the options
        :return:
        """
        return None

    def process_results(self,
                        discovery: Discovery,
                        options: dict,
                        results: list) -> None:
        """
        Process the results list
        :param discovery: the Discovery object that launched the scanner
        :param options: dictionary containing the options
        :param results: list of results to process
        :return: None
        """
        pass

    def print(self,
              message: str) -> None:
        """
        Print a message to the console
        :param message:
        :return:
        """
        self.stdout.write(message)
