from loguru import logger
from dotenv import load_dotenv
import sys
import os
import x

load_dotenv()

logger.remove()
logger.add(sys.stderr, level=os.getenv("LOG_LEVEL", "INFO"))
logger.info("Hello World")
x.fun()