from coloredLogger import ColoredLogger
from timeLogger import TimeLogger
from logLevel import LogLevel
import time

class ColoredTimeLogger(ColoredLogger, TimeLogger):

    def __init__(self, level: LogLevel):
        self.level = level
    
    def log(self, level: LogLevel, message: str):
        if (level.value >= self.level.value):
            t = time.localtime()
            print(ColoredLogger.colorMap[level], f"[{t.tm_hour:>02}:{t.tm_min:>02}:{t.tm_sec:>02}][{level.name}] {message}", ColoredLogger.RESET)