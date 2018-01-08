#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coder: samren
# version : 1.0
import os
import time
import logging
import logging.handlers


class Logger(object):
    def __init__(self, logname='./log/logger.log', loglevel=logging.INFO):
        """
           指定保存日志的文件路径，日志级别，以及调用文件
           将日志存入到指定的文件中
        """

        # 创建一个logger
        self.logger = logging.getLogger()
        self.logger.setLevel(loglevel)

        # 创建一个文件handler，用于写入日志文件
        # 每小时滚动一次日志文件，防止日志文件太大
        fh = logging.handlers.TimedRotatingFileHandler(logname)
        # 设置后缀名称，跟strftime的格式一样
        fh.suffix = "%Y%m%d-%H.log"
        #fh = logging.FileHandler(logname)
        fh.setLevel(loglevel)

        # 再创建一个流handler，用于输出到控制台command
        ch = logging.StreamHandler()
        ch.setLevel(loglevel)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(filename)s:%(lineno)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s')
        #fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger


if __name__ == '__main__':
    logger = Logger("product.log", logging.DEBUG).getlog()
    logger.info('info message')
    logger.error("error message")
    logger.warning("warn message")
    logger.critical("critical message")