#!/usr/bin/env python3

class Lights:
    def toggle(light):
        import requests
        import configparser
        import json
        
        config = configparser.ConfigParser()
        config.read('/home/wes/.keys')
        
        token = config['lifx']['token']
        
        headers = {
            "Authorization": "Bearer %s" % token,
        }
        
        response = requests.post(f"https://api.lifx.com/v1/lights/{light}/toggle", headers=headers)
