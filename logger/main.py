from coloredTimeLogger import ColoredTimeLogger, LogLevel
import time

logger = ColoredTimeLogger(LogLevel.WARN)

logger.debug("debug message")
logger.info("info message")
logger.warn("warn message")
logger.error("error message")
