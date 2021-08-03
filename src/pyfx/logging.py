"""
Separate file for logging configuration.
"""
from loguru import logger


def setup_logger():
    """Set up """
    logger.remove()
    logger.add(
        "/tmp/pyfx.log",
        level='DEBUG',
        rotation='5MB',
        retention="10 days",
        format="<green>{time}</green> {module}.{function} "
               "<level>{message}</level>"
    )
