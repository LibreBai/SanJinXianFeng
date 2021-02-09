# -*- coding=utf-8 -*-

import os

import logging
from logging import handlers

DEFAULT_LOG_FILE = "./log/sjxf.log"


class SjxfLog:

    def __init__(self, file_name=DEFAULT_LOG_FILE):

        # 判断存放日志目录是否存在
        if not os.path.exists(file_name):
            os.mkdir(os.path.dirname(file_name))

        self.__log = logging.getLogger()

        # 设置日志文件以及各种格式
        log_file_handler = logging.handlers.RotatingFileHandler(file_name)

        log_format_str = "[%(asctime)s] [%(levelname)s] [%(filename)s] " \
                         "[line:%(lineno)d] %(message)s"
        date_format_str = "%Y-%m-%d %H:%M:%S"

        log_format = logging.Formatter(fmt=log_format_str,
                                       datefmt=date_format_str)
        
        log_file_handler.setFormatter(log_format)
        
        self.__log.addHandler(log_file_handler)

        #
        self.__log.setLevel(logging.DEBUG)


    def debug(self, msg):
        self.__log.debug(msg)

    def error(self, msg):
        self.__log.error(msg)

    def info(self, msg):
        self.__log.info(msg)
