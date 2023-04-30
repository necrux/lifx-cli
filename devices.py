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
            label     = response[key]["label"]
            ident     = response[key]["id"]
            power     = response[key]["power"]
            connected = response[key]["connected"]
            group     = response[key]["group"]["name"]

            devices += [[label, ident, power, connected, group]]
        
        devices.sort()
        print(tabulate(devices, headers=["Name", "ID", "State", "Connected", "Group"]))
