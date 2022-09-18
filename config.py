import configparser
import logging
from typing import Dict, Optional
from log_subsystem import debug_file_handler, debug_console_handler


class Config:
    def __init__(self, config_path) -> None:
        """
        Init class and load config.
        If ini file not found on filepath will create and load default config.
        """
        self.__logger__ = logging.getLogger(__name__)
        self.__logger__.setLevel(logging.DEBUG)
        self.__logger__.addHandler(debug_file_handler)
        self.__logger__.addHandler(debug_console_handler)

        self.__config__ = configparser.ConfigParser()
        try:
            with open(config_path, 'r', encoding='utf-8') as config_file:
                self.__config__.read_file(config_file)
                self.__logger__.info('config was loaded')
        except FileNotFoundError as exception:
            self.__logger__.warning('config file %s not found', config_path)
            raise exception

    def get_config(self, config_name: Optional[str] = None) -> Dict:
        """
        Return config section. If config_name not set, return all config.
        """
        if config_name:
            return self.__config__[config_name]
        else:
            return self.__config__


if __name__ == '__main__':
    config = Config('config.ini')
    print(config.get_config('BASE'))
