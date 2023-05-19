#!/usr/bin/env python3
"""Control LIFX lights and effects."""
import sys
import json
from requests import get, post, put
from tabulate import tabulate
from src.lifx.auth import Auth

API = 'https://api.lifx.com/v1'


class Lights:
    """Control LIFX lights and effects."""

    def __init__(self):
        self.auth = Auth()
        self.auth_headers = self.auth.auth()

    def get(self):
        """Print a list of all LIFX devices on this account."""

        url = f'{API}/lights/all'
        response = get(url, headers=self.auth_headers, timeout=5)

        if response.status_code != 200:
            print(f"HTTP request failed. State code: {response.status_code}")
            sys.exit(30)

        response = json.loads(response.content)

        devices = []

        for _, value in enumerate(response):
            label = value["label"]
            ident = value["id"]
            power = value["power"]
            connected = value["connected"]
            group = value["group"]["name"]
            group_id = value["group"]["id"]

            devices += [[label, ident, power, connected, group, group_id]]

        devices.sort()
        print(tabulate(devices, headers=["Name", "ID", "State", "Connected", "Group", "Group ID"]))

    def toggle(self, light_id, group):
        """Toggles the power for the specified light. Requires the device ID."""

        if group:
            light_id = f'group_id:{light_id}'

        url = f"{API}/lights/{light_id}/toggle"
        response = post(url, headers=self.auth_headers, timeout=5)

        if response.status_code != 207:
            print(f"HTTP request failed. State code: {response.status_code}")
            sys.exit(31)
        else:
            sys.exit(0)

    def set_state(self, light_id, group, color, state_attributes):
        """Changes the state for the specified light. Requires the device ID."""

        payload = {
            "power": f"{state_attributes['power']}",
            "color": f"{color}",
            "brightness": f"{state_attributes['brightness']}",
            "duration": f"{state_attributes['duration']}",
            "infrared": f"{state_attributes['infrared']}",
        }

        if group:
            light_id = f'group_id:{light_id}'

        url = f"{API}/lights/{light_id}/state"
        response = put(url, data=payload, headers=self.auth_headers, timeout=5)

        if response.status_code != 207:
            print(f"HTTP request failed. State code: {response.status_code}")
            sys.exit(32)
        else:
            sys.exit(0)

    def clean(self, light_id, group, duration):
        """Switches a light to clean mode. Requires the device ID."""

        if group:
            light_id = f'group_id:{light_id}'

        payload = {
            "stop": "False",
            "duration": f"{duration}",
        }

        url = f"{API}/lights/{light_id}/clean"
        response = post(url, data=payload, headers=self.auth_headers, timeout=5)

        if response.status_code != 207:
            print(f"HTTP request failed. State code: {response.status_code}")
            sys.exit(33)
        else:
            sys.exit(0)
