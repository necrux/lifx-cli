#!/usr/bin/env python3
"""Control LIFX lights and effects."""

from requests import post, put
from tabulate import tabulate
from src.lifx.auth import Auth


class Lights:
    """Control LIFX lights and effects."""

    def __init__(self):
        self.auth = Auth()
        self.auth_headers = self.auth.auth()

    def toggle(self, light_id, group):
        """Toggles the power for the specified light. Requires the device ID."""

        if group:
            light_id = f'group_id:{light_id}'

        url = f"https://api.lifx.com/v1/lights/{light_id}/toggle"
        post(url, headers=self.auth_headers, timeout=5)

    def set_state(self, light_id, group, color, power, brightness, duration, infrared):
        """Changes the state for the specified light. Requires the device ID."""

        payload = {
            "power": f"{power}",
            "color": f"{color}",
            "brightness": f"{brightness}",
            "duration": f"{duration}",
            "infrared": f"{infrared}",
        }

        if group:
            light_id = f'group_id:{light_id}'

        url = f"https://api.lifx.com/v1/lights/{light_id}/state"
        put(url, data=payload, headers=self.auth_headers, timeout=5)

    def list_effects(self):
        """List effects currently supported by the CLI."""
        effects = [['Breathe',
                    'Performs a breathe effect by slowly fading between the given colors.'],
                   ['Pulse',
                    'Performs a pulse effect by quickly flashing between the given colors. ']]

        print(tabulate(effects, headers=["Name", "Description"]))
        print("\nNote: The CLI can only control effects stored on your light's firmware.")

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

        url = f"https://api.lifx.com/v1/lights/{light_id}/effects/breathe"
        post(url, data=data, headers=self.auth_headers, timeout=5)

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

        url = f"https://api.lifx.com/v1/lights/{light_id}/effects/pulse"
        post(url, data=data, headers=self.auth_headers, timeout=5)

    def stop_effect(self, light_id, group):
        """Stop all effects on the specified light. Requires Light ID."""

        data = {
            "power_off": True
        }

        if group:
            light_id = f'group_id:{light_id}'

        url = f"https://api.lifx.com/v1/lights/{light_id}/effects/off"
        post(url, data=data, headers=self.auth_headers, timeout=5)