#!/usr/bin/env python3
"""Control LIFX effects."""
import sys
from requests import post
from tabulate import tabulate
from src.lifx.auth import Auth

API = 'https://api.lifx.com/v1'
EFFECTS = [['Breathe',
            'Performs a breathe effect by slowly fading between the given colors.'],
           ['Pulse',
            'Performs a pulse effect by quickly flashing between the given colors. ']]
EFFECTS_NOTICE = "Note: The CLI can only control effects stored on your light's firmware."


class Effects:
    """Control LIFX effects."""
    def __init__(self):
        self.auth = Auth()
        self.auth_headers = self.auth.auth()

    @staticmethod
    def list_effects():
        """List effects currently supported by the CLI."""
        print(tabulate(EFFECTS, headers=["Name", "Description"]))
        print(f"\n{EFFECTS_NOTICE}")

    def breathe_effect(self, light_id, group, color):
        """Activates the breath effect (period: 2; cycles: 10).
        Requires the device ID and color."""

        if len(color) == 1:
            data = {
                "period": 2,
                "cycles": 10,
                "color": f"{color[0]}",
            }
        else:
            data = {
                "period": 2,
                "cycles": 10,
                "from_color": f"{color[0]}",
                "color": f"{color[1]}",
            }

        if group:
            light_id = f'group_id:{light_id}'

        url = f"{API}/lights/{light_id}/effects/breathe"
        response = post(url, data=data, headers=self.auth_headers, timeout=5)

        if response.status_code != 207:
            print(f"HTTP request failed. State code: {response.status_code}")
            sys.exit(20)
        else:
            sys.exit(0)

    def pulse_effect(self, light_id, group, color):
        """Activates the pulse effect (period: 2; cycles: 10).
        Requires the device ID and color."""

        if len(color) == 1:
            data = {
                "period": 2,
                "cycles": 10,
                "color": f"{color[0]}",
            }
        else:
            data = {
                "period": 2,
                "cycles": 10,
                "from_color": f"{color[0]}",
                "color": f"{color[1]}",
            }

        if group:
            light_id = f'group_id:{light_id}'

        url = f"{API}/lights/{light_id}/effects/pulse"
        response = post(url, data=data, headers=self.auth_headers, timeout=5)

        if response.status_code != 207:
            print(f"HTTP request failed. State code: {response.status_code}")
            sys.exit(21)
        else:
            sys.exit(0)

    def stop_effect(self, light_id, group):
        """Stop all effects on the specified light. Requires Light ID."""

        data = {
            "power_off": True
        }

        if group:
            light_id = f'group_id:{light_id}'

        url = f"{API}/lights/{light_id}/effects/off"
        response = post(url, data=data, headers=self.auth_headers, timeout=5)

        if response.status_code != 207:
            print(f"HTTP request failed. State code: {response.status_code}")
            sys.exit(22)
        else:
            sys.exit(0)
