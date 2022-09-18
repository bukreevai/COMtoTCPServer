import logging
from datetime import datetime


common_formatter = logging.Formatter(
    '%(asctime)s  %(filename)s  %(levelname)s: %(message)s'
    )
now = datetime.now().strftime("%Y_%m_%d")
debug_file_handler = logging.FileHandler(f'{now}.log')
debug_file_handler.setLevel(logging.DEBUG)
debug_file_handler.setFormatter(common_formatter)

debug_console_handler = logging.StreamHandler()
debug_console_handler.setLevel(logging.DEBUG)
debug_console_handler.setFormatter(common_formatter)
