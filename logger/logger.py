from logLevel import LogLevel

class Logger:

    def __init__(self, level: LogLevel):
        self.level = level
    
    def log(self, level: LogLevel, message: str):
        if (level.value >= self.level.value):
            print(f"[{level.name}] {message}")
    
    def debug(self, message: str):
        self.log(LogLevel.DEBUG, message)
    
    def info(self, message: str): 
        self.log(LogLevel.INFO, message)
    
    def warn(self, message: str):
        self.log(LogLevel.WARN, message)
    
    def error(self, message: str):
        self.log(LogLevel.ERROR, message)
