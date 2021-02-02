import logging

logging.basicConfig(level=logging.DEBUG, filename='file_output.log', format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d@%(filename)s - %(message)s')
logger = logging.getLogger(__name__)

logger.debug("This is debug.")
logger.info("This is info")
logger.warning("This is warnning.")
logger.error("This is error.")
logger.critical("This is critical")
