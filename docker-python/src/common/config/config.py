#########################################################
# Builtin packages
#########################################################
from configparser import ConfigParser

#########################################################
# 3rd party packages
#########################################################

#########################################################
# Own packages
#########################################################
from utils import Singleton


class Config(Singleton):
    def __init__(self):
        self.config_file = 'common/config/config.ini'

    def get_config(self) -> ConfigParser:
        config = ConfigParser()
        config.read(self.config_file, encoding="utf-8")
        return config
