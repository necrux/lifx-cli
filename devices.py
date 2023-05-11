#!/usr/bin/env python3

class Devices:
    def get(self):
        """Print a list of all LIFX devices on this account."""
        import requests
        import json
        from tabulate import tabulate
        from auth import Auth

        auth = Auth()
        auth_headers = auth.auth()

        response = requests.get('https://api.lifx.com/v1/lights/all', headers=auth_headers)
        response = json.loads(response.content)

        devices = []

        for key in range(0, len(response)):
            label = response[key]["label"]
            ident = response[key]["id"]
            power = response[key]["power"]
            connected = response[key]["connected"]
            group = response[key]["group"]["name"]
            group_id = response[key]["group"]["id"]

            devices += [[label, ident, power, connected, group, group_id]]

        devices.sort()
        print(tabulate(devices, headers=["Name", "ID", "State", "Connected", "Group", "Group ID"]))
