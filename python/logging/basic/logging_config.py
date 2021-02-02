import yaml
import logging
import logging.config

def config_logging(default_path='config.yaml'):
    with open(default_path, 'r') as f:
            config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

config_logging()
logger = logging.getLogger(__name__)

logger.debug("This is A debug.")
logger.info("This is A info")
logger.warning("This is A warnning.")
logger.error("This is A error.")
logger.critical("This is A critical")