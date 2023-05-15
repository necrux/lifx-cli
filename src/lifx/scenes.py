#!/usr/bin/env python3
"""List and control LIFX scenes."""

import json
from requests import get, put
from tabulate import tabulate
from src.lifx.auth import Auth


class Scenes:
    """List and control LIFX scenes."""

    def __init__(self):
        self.auth = Auth()
        self.auth_headers = self.auth.auth()

    def get(self):
        """Print a list of all scenes on this account."""

        url = 'https://api.lifx.com/v1/scenes'
        response = get(url, headers=self.auth_headers, timeout=5)
        response = json.loads(response.content)

        scenes = []

        for key in range(len(response)):
            scenes += [[response[key]["name"], response[key]["uuid"]]]

        scenes.sort()
        print(tabulate(scenes, headers=["Name", "ID"]))

    def activate(self, scene_id):
        """Activates the specified scene. Requires scene UUID."""

        url = f'https://api.lifx.com/v1/scenes/scene_id:{scene_id}/activate'
        put(url, headers=self.auth_headers, timeout=5)
