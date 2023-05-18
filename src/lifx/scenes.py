#!/usr/bin/env python3
"""List and control LIFX scenes."""
import sys
import json
from requests import get, put
from tabulate import tabulate
from src.lifx.auth import Auth

API = 'https://api.lifx.com/v1'


class Scenes:
    """List and control LIFX scenes."""

    def __init__(self):
        self.auth = Auth()
        self.auth_headers = self.auth.auth()

    def get(self):
        """Print a list of all scenes on this account."""

        url = f'{API}/scenes'
        response = get(url, headers=self.auth_headers, timeout=5)

        if response.status_code != 200:
            print(f"HTTP request failed. State code: {response.status_code}")
            sys.exit(40)

        response = json.loads(response.content)

        scenes = []

        for _, value in enumerate(response):
            scenes += [[value["name"], value["uuid"]]]

        scenes.sort()
        print(tabulate(scenes, headers=["Name", "ID"]))

    def activate(self, scene_id):
        """Activates the specified scene. Requires scene UUID."""

        url = f'{API}/scenes/scene_id:{scene_id}/activate'
        response = put(url, headers=self.auth_headers, timeout=5)

        if response.status_code != 207:
            print(f"HTTP request failed. State code: {response.status_code}")
            sys.exit(41)
        else:
            sys.exit(0)
