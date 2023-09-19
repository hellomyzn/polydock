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
        self.__config = self.__initialize()

    @property
    def config(self) -> ConfigParser:
        """Getter for __config

        Returns:
            self.__config (ConfigParser): Private property __config
        """
        return self.__config

    def __initialize(self) -> ConfigParser:
        config_file = 'common/config/config.ini'

        if self.__config is not None:
            return self.__config

        config = ConfigParser()
        config.read(config_file, encoding="utf-8")

        return config
