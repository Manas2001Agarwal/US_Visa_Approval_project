from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys
import os

logging.info("custom_logging")

try :
    a = 1/0
except Exception as e:
    logging.info(e)
    raise USvisaException(e,sys)