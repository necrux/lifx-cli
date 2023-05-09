#!/usr/bin/env python3

class Auth:
    def auth(self):
        import configparser
        
        config = configparser.ConfigParser()
        config.read('/home/wes/.keys')
        
        token = config['lifx']['token']
        
        headers = {
            "Authorization": "Bearer %s" % token,
        }

        return headers
