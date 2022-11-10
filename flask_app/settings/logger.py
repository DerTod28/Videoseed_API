import logging
import sys

logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger('Service-logger')
logger.setLevel(logging.DEBUG)
