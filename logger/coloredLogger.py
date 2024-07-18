from logger import Logger
from logLevel import LogLevel

class ColoredLogger(Logger):

    RESET = "\033[0m"
    RED = "\033[31m"
    BLUE = "\033[34m"
    YELLOW = "\033[93m"
    GREEN = "\033[32m"
    colorMap = {LogLevel.DEBUG: BLUE, LogLevel.INFO: GREEN, LogLevel.WARN: YELLOW, LogLevel.ERROR: RED}

    def __init__(self, level: LogLevel):
        super().__init__(level)
    
    def log(self, level: LogLevel, message: str):
        if (level.value >= self.level.value):
            print(ColoredLogger.colorMap[level], f"[{level.name}] {message}", ColoredLogger.RESET)