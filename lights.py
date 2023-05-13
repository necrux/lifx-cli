#!/usr/bin/env python3

class Lights:

    def __init__(self):
        from auth import Auth

        self.auth = Auth()
        self.auth_headers = self.auth.auth()

    def toggle(self, light_id, group):
        """Toggles the power for the specified light. Requires the device ID."""
        from requests import post

        if group:
            light_id = f'group_id:{light_id}'

        post(f"https://api.lifx.com/v1/lights/{light_id}/toggle", headers=self.auth_headers)

    def set_state(self, light_id, group, color, power, brightness, duration, infrared):
        """Changes the state for the specified light. Requires the device ID as well as optional changes."""
        from requests import put

        payload = {
            "power": f"{power}",
            "color": f"{color}",
            "brightness": f"{brightness}",
            "duration": f"{duration}",
            "infrared": f"{infrared}",
        }

        if group:
            light_id = f'group_id:{light_id}'

        put(f"https://api.lifx.com/v1/lights/{light_id}/state", data=payload, headers=self.auth_headers)

    def list_effects(self):
        """List effects currently supported by the CLI."""
        from tabulate import tabulate

        effects = [['Breathe', 'Performs a breathe effect by slowly fading between the given colors.'],
                   ['Pulse', 'Performs a pulse effect by quickly flashing between the given colors. ']]

        print(tabulate(effects, headers=["Name", "Description"]))
        print("\nNote: The CLI can only control effects stored on your light's firmware.")
        pass

    def breathe_effect(self, light_id, group, color):
        """Activates the breath effect on the specified light (period: 2; cycles: 10). Requires the device ID and
        color."""
        from requests import post

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

        post(f"https://api.lifx.com/v1/lights/{light_id}/effects/breathe", data=data, headers=self.auth_headers)

    def pulse_effect(self, light_id, group, color):
        """Activates the pulse effect on the specified light (period: 2; cycles: 10). Requires the device ID and
        color."""
        from requests import post

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

        post(f"https://api.lifx.com/v1/lights/{light_id}/effects/pulse", data=data, headers=self.auth_headers)

    def stop_effect(self, light_id, group):
        """Stop all effects on the specified light. Requires Light ID."""
        from requests import post

        data = {
            "power_off": True
        }

        if group:
            light_id = f'group_id:{light_id}'

        post(f"https://api.lifx.com/v1/lights/{light_id}/effects/off", data=data, headers=self.auth_headers)
