# -*- coding: utf-8 -*-

import pprint
import yaml
import os
import shotgun_api3

CONFIG_FILE = "shotgun-desktop-timelog-config.yml"


class Config(object):
    address = None
    login_name = None
    login_password = None
    limit = None
    project_name = None

    def __init__(self):
        config_path = os.path.abspath(os.path.join(os.getcwd(), CONFIG_FILE))
        pprint.pprint(config_path)
        with open(config_path) as f:
            self.config = yaml.load(f, Loader=yaml.FullLoader)

        self.address = self.config["shotgun-address"]
        self.login_name = self.config["login-name"]
        self.login_password = self.config["login-password"]
        self._sg = None

    def print_config(self):
        pprint.pprint(self.config)

    def login(self):
        '''
        login to shotgun server
        :return: Shotgun instance
        '''
        self._sg = shotgun_api3.Shotgun(self.address, login=self.login_name, password=self.login_password)
        return self._sg
