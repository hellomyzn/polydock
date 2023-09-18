"""common.config.Config"""
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
    __config = None

    def __init__(self):
        self.__config_file = 'common/config/config.ini'

        if self.__config is None:
            self.__config = ConfigParser()
            self.__config.read(self.__config_file, encoding="utf-8")

    def get_config(self) -> ConfigParser:
        """Getter for __config

        Returns:
            self.__config (ConfigParser): Private property __config
        """
        return self.__config
