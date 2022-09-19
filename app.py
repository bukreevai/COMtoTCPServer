"""
Main app module
"""
import logging

from configuration import Config
from log_subsystem import debug_console_handler, debug_file_handler


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(debug_file_handler)
logger.addHandler(debug_console_handler)

config = Config('config.ini')
web_server_config = config.get_config('WEB_SERVER')
tcp_server_config = config.get_config('TCP_SERVER')
serial_config = config.get_config('SERIAL')
app_config = config.get_config('BASE')

log_level = app_config.get('log_level')
