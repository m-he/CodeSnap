import logging

logger = logging.getLogger('A.a')
logger.setLevel(logging.DEBUG)


def log():
    logger.debug("This is A.a debug.")
    logger.info("This is A.a info")
    logger.warning("This is A.a warnning.")
    logger.error("This is A.a error.")
    logger.critical("This is A.a critical")
