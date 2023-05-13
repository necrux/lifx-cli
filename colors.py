#!/usr/bin/env python3

COLOR_TABLE = [['[name]', 'white, red, orange, yellow, cyan, green, blue, purple, or pink', 'Sets hue and '
                                                                                            'saturation only.'],
               ['hue:[0-360]', 'hue:120', 'Sets hue.'],
               ['saturation:[0.0-1.0]', 'saturation:0.5', 'Sets saturation.'],
               ['brightness:[0.0-1.0]', 'brightness:0.5', 'Sets brightness.'],
               ['kelvin:[1500-9000]', 'kelvin:5000', 'Sets kelvin to -c and saturation to 0.0.'],
               ['#RRGGBB', '#ff0000', 'Converts to HSBK.'],
               ['rgb:[0-255],[0-255],[0-255]', 'rgb:255,255,0', '	Converts to HSBK.']]


class Colors:
    def __init__(self):
        from auth import Auth

        self.auth = Auth()
        self.auth_headers = self.auth.auth()

    @staticmethod
    def color_information():
        """Print color formatting information."""
        from tabulate import tabulate

        print(tabulate(COLOR_TABLE, headers=["Format", "Example", "Notes"]))

    def validate_color(self, color):
        """Validate the provided color with the LIFX API."""
        import json
        from requests import get
        from tabulate import tabulate

        response = get(f'https://api.lifx.com/v1/color?string={color}', headers=self.auth_headers)
        response = json.loads(response.content)

        hue = response['hue'] or 'None'
        saturation = response['saturation'] or 'None'
        brightness = response['brightness'] or 'None'
        kelvin = response['kelvin'] or 'None'

        validated_colors = [[hue, saturation, brightness, kelvin]]

        print(tabulate(validated_colors, headers=["Hue", "Saturation", "Brightness", "Kelvin"]))
        pass
