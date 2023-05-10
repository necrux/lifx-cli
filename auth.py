#!/usr/bin/env python3

class Auth:
    def auth(self):
        """Returns the authentication headers to authenticate to LIFX."""
        import configparser
        from os import environ, getenv

        if environ.get('LIFX'):
            token = getenv('LIFX')
        else:
            config = configparser.ConfigParser()
            config.read('/home/wes/.keys')

            token = config['lifx']['token']
        
        headers = {
            "Authorization": "Bearer %s" % token,
        }

        return headers
