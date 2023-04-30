#!/usr/bin/env python3

class Devices:
    def get():
        import requests
        import json
        from tabulate import tabulate
        from auth import Auth

        auth = Auth.auth()

        response = requests.get('https://api.lifx.com/v1/lights/all', headers=auth)
        response = json.loads(response.content)
        
        devices = []
        
        for key in range(0, len(response)):
            devices += [[response[key]["label"], response[key]["id"],response[key]["power"], response[key]["connected"]]]
        
        devices.sort()
        print(tabulate(devices, headers=["Name", "ID", "State", "Connected"]))
