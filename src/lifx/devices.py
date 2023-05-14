#!/usr/bin/env python3
"""List LIFX devices"""

import json
from requests import get
from tabulate import tabulate
from src.lifx.auth import Auth


class Devices:
    """List LIFX devices."""

    def __init__(self):
        self.auth = Auth()
        self.auth_headers = self.auth.auth()

    def get(self):
        """Print a list of all LIFX devices on this account."""

        url = 'https://api.lifx.com/v1/lights/all'
        response = get(url, headers=self.auth_headers, timeout=5)
        response = json.loads(response.content)

        devices = []

        for key in enumerate(response):
            label = response[key]["label"]
            ident = response[key]["id"]
            power = response[key]["power"]
            connected = response[key]["connected"]
            group = response[key]["group"]["name"]
            group_id = response[key]["group"]["id"]

            devices += [[label, ident, power, connected, group, group_id]]

        devices.sort()
        print(tabulate(devices, headers=["Name", "ID", "State", "Connected", "Group", "Group ID"]))
