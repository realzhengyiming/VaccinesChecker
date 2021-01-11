import logging.handlers
import os
import sys

from loguru import logger


class LogUtil:
    __instance = None

    def __new__(cls):
        if not cls.__instance:
            return cls.__instance
        else:
            LOG_FILE = os.path.expanduser("vaccines_checker_{time}.log")

            logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")
            file_handler = logging.handlers.RotatingFileHandler(LOG_FILE, encoding="utf-8")
            logger.add(file_handler)

            cls.__instance = logger
            return cls.__instance


logger_instance = LogUtil()
