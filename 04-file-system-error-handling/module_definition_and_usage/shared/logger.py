import os
import re
import sys
import logging


def striplines(m):
    m = re.compile(r'[\t]').sub(' ', str(m))
    return re.compile(r'[\r\n]').sub('', str(m))


def ex(e):
    logger.exception(striplines(e))


def info(msg):
    logger.info(msg)


def err(msg):
    logger.error(msg)


def debug(msg):
    logger.debug(msg)


logger = logging.getLogger(__name__)
stage = os.getenv("STAGE", 'dev')
if stage == 'dev' or stage == 'local':
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.WARN)

logger.propagate = False  # remove default logger
if logger.handlers:
    for handler in logger.handlers:
        logger.removeHandler(handler)

handler = logging.StreamHandler(sys.stdout)

formatter=logging.Formatter(
    fmt="[%(asctime)s] %(levelname)-6s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")

handler.setFormatter(formatter)

logger.addHandler(handler)
