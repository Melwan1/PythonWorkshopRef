from logger import Logger
from logLevel import LogLevel
import time

class TimeLogger(Logger):

    def __init__(self, level: LogLevel):
        super().__init__(level)
    
    def log(self, level: LogLevel, message: str):
        if (level.value >= self.level.value):
            t = time.localtime()
            print(f"[{t.tm_hour:>02}:{t.tm_min:>02}:{t.tm_sec:>02}][{level.name}] {message}")