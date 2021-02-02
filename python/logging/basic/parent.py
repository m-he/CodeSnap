import logging
import sys
import child

logger = logging.getLogger('A')
logger.setLevel(logging.WARNING)

handler = logging.FileHandler('parent_child_out.log')
formatter = logging.Formatter('From Parent Handler %(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.debug("This is A debug.")
logger.info("This is A info")
logger.warning("This is A warnning.")
logger.error("This is A error.")
logger.critical("This is A critical")
child.log()
