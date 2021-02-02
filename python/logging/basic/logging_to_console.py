import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logger.debug("This is debug.")
logger.info("This is info")
logger.warning("This is warnning.")
logger.error("This is error.")
logger.critical("This is critical")

try:
    result = 5 / 0
except Exception as e:
    logger.error('Some errors', exc_info=True)
