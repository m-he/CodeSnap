import logging
import sys

CONSOLE_LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(lineno)d@%(filename)s - %(message)s'
FILE_LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(process)d - %(lineno)d@%(filename)s - %(message)s'

logging.basicConfig(format=CONSOLE_LOG_FORMAT)
logging.root.handlers[0].setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# FileHandler
file_handler = logging.FileHandler('logging_to_both_console_file.log')
formatter = logging.Formatter(FILE_LOG_FORMAT)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

logger.debug("This is debug.")
logger.info("This is info")
logger.warning("This is warnning.")
logger.error("This is error.")
logger.critical("This is critical")