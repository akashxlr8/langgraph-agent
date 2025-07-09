import sys
from loguru import logger

def configure_logger():
    logger.remove()
    logger.add(sys.stderr, level="INFO")
    # Use enqueue=True to write logs in a background thread (non-blocking for ASGI)
    logger.add("logs/app.log", rotation="500 MB", level="DEBUG", serialize=True, enqueue=True)
    return logger

log = configure_logger()
