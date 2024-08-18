from logLevel import LogLevel
from logger import Logger
from coloredLogger import ColoredLogger
from timeLogger import TimeLogger
from coloredTimeLogger import ColoredTimeLogger
import time

def test_log_level_debug_less_than_info():
    assert LogLevel.DEBUG.value < LogLevel.INFO.value

def test_log_level_info_less_than_warn():
    assert LogLevel.INFO.value < LogLevel.WARN.value

def test_log_level_warn_less_than_error():
    assert LogLevel.WARN.value < LogLevel.ERROR.value

def test_logger_init_sets_level_debug():
    logger = Logger(LogLevel.DEBUG)
    assert logger.level == LogLevel.DEBUG

def test_logger_init_sets_level_info():
    logger = Logger(LogLevel.INFO)
    assert logger.level == LogLevel.INFO

def test_logger_init_sets_level_warn():
    logger = Logger(LogLevel.WARN)
    assert logger.level == LogLevel.WARN

def test_logger_init_sets_level_error():
    logger = Logger(LogLevel.ERROR)
    assert logger.level == LogLevel.ERROR

def test_logger_log_debug_with_level_debug(capsys):
    logger = Logger(LogLevel.DEBUG)
    logger.log(LogLevel.DEBUG, "This is a debug message")
    out, _ = capsys.readouterr()
    assert out == "[DEBUG] This is a debug message\n"

def test_logger_log_debug_with_level_info(capsys):
    logger = Logger(LogLevel.INFO)
    logger.log(LogLevel.DEBUG, "This is a debug message")
    out, _ = capsys.readouterr()
    assert out == ""

def test_logger_log_debug_with_level_warn(capsys):
    logger = Logger(LogLevel.WARN)
    logger.log(LogLevel.DEBUG, "This is a debug message")
    out, _ = capsys.readouterr()
    assert out == ""

def test_logger_log_debug_with_level_error(capsys):
    logger = Logger(LogLevel.ERROR)
    logger.log(LogLevel.DEBUG, "This is a debug message")
    out, _ = capsys.readouterr()
    assert out == ""

def test_logger_log_info_with_level_debug(capsys):
    logger = Logger(LogLevel.DEBUG)
    logger.log(LogLevel.INFO, "This is an info message")
    out, _ = capsys.readouterr()
    assert out == "[INFO] This is an info message\n"

def test_logger_log_info_with_level_info(capsys):
    logger = Logger(LogLevel.INFO)
    logger.log(LogLevel.INFO, "This is an info message")
    out, _ = capsys.readouterr()
    assert out == "[INFO] This is an info message\n"

def test_logger_log_info_with_level_warn(capsys):
    logger = Logger(LogLevel.WARN)
    logger.log(LogLevel.INFO, "This is an info message")
    out, _ = capsys.readouterr()
    assert out == ""

def test_logger_log_info_with_level_error(capsys):
    logger = Logger(LogLevel.ERROR)
    logger.log(LogLevel.INFO, "This is an info message")
    out, _ = capsys.readouterr()
    assert out == ""

def test_logger_log_warn_with_level_debug(capsys):
    logger = Logger(LogLevel.DEBUG)
    logger.log(LogLevel.WARN, "This is a warn message")
    out, _ = capsys.readouterr()
    assert out == "[WARN] This is a warn message\n"

def test_logger_log_warn_with_level_info(capsys):
    logger = Logger(LogLevel.INFO)
    logger.log(LogLevel.WARN, "This is a warn message")
    out, _ = capsys.readouterr()
    assert out == "[WARN] This is a warn message\n"

def test_logger_log_warn_with_level_warn(capsys):
    logger = Logger(LogLevel.WARN)
    logger.log(LogLevel.WARN, "This is a warn message")
    out, _ = capsys.readouterr()
    assert out == "[WARN] This is a warn message\n"

def test_logger_log_warn_with_level_error(capsys):
    logger = Logger(LogLevel.ERROR)
    logger.log(LogLevel.WARN, "This is a warn message")
    out, _ = capsys.readouterr()
    assert out == ""

def test_logger_log_error_with_level_debug(capsys):
    logger = Logger(LogLevel.DEBUG)
    logger.log(LogLevel.ERROR, "This is an error message")
    out, _ = capsys.readouterr()
    assert out == "[ERROR] This is an error message\n"

def test_logger_log_error_with_level_info(capsys):
    logger = Logger(LogLevel.INFO)
    logger.log(LogLevel.ERROR, "This is an error message")
    out, _ = capsys.readouterr()
    assert out == "[ERROR] This is an error message\n"

def test_logger_log_error_with_level_warn(capsys):
    logger = Logger(LogLevel.WARN)
    logger.log(LogLevel.ERROR, "This is an error message")
    out, _ = capsys.readouterr()
    assert out == "[ERROR] This is an error message\n"

def test_logger_log_error_with_level_error(capsys):
    logger = Logger(LogLevel.ERROR)
    logger.log(LogLevel.ERROR, "This is an error message")
    out, _ = capsys.readouterr()
    assert out == "[ERROR] This is an error message\n"

def test_logger_debug_should_be_same_as_log_debug(capsys):
    logger = Logger(LogLevel.DEBUG)
    logger.debug("This is a debug message")
    out, _ = capsys.readouterr()
    assert out == "[DEBUG] This is a debug message\n"

def test_logger_info_should_be_same_as_log_info(capsys):
    logger = Logger(LogLevel.DEBUG)
    logger.info("This is an info message")
    out, _ = capsys.readouterr()
    assert out == "[INFO] This is an info message\n"

def test_logger_warn_should_be_same_as_log_warn(capsys):
    logger = Logger(LogLevel.DEBUG)
    logger.warn("This is a warn message")
    out, _ = capsys.readouterr()
    assert out == "[WARN] This is a warn message\n"

def test_logger_error_should_be_same_as_log_error(capsys):
    logger = Logger(LogLevel.DEBUG)
    logger.error("This is an error message")
    out, _ = capsys.readouterr()
    assert out == "[ERROR] This is an error message\n"

def test_logger_multiple_logs_with_level_debug(capsys):
    logger = Logger(LogLevel.DEBUG)
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warn("This is a warn message")
    logger.error("This is an error message")
    out, _ = capsys.readouterr()
    assert out == "[DEBUG] This is a debug message\n[INFO] This is an info message\n[WARN] This is a warn message\n[ERROR] This is an error message\n"

def test_logger_multiple_logs_with_level_info(capsys):
    logger = Logger(LogLevel.INFO)
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warn("This is a warn message")
    logger.error("This is an error message")
    out, _ = capsys.readouterr()
    assert out == "[INFO] This is an info message\n[WARN] This is a warn message\n[ERROR] This is an error message\n"

def test_logger_multiple_logs_with_level_warn(capsys):
    logger = Logger(LogLevel.WARN)
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warn("This is a warn message")
    logger.error("This is an error message")
    out, _ = capsys.readouterr()
    assert out == "[WARN] This is a warn message\n[ERROR] This is an error message\n"

def test_logger_multiple_logs_with_level_error(capsys):
    logger = Logger(LogLevel.ERROR)
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warn("This is a warn message")
    logger.error("This is an error message")
    out, _ = capsys.readouterr()
    assert out == "[ERROR] This is an error message\n"

def test_colored_logger_debug_color(capsys):
    coloredLogger = ColoredLogger(LogLevel.DEBUG)
    coloredLogger.debug("What a wonderful debug message")
    out, _ = capsys.readouterr()
    assert out == "\033[34m[DEBUG] What a wonderful debug message\033[0m\n"

def test_colored_logger_info_color(capsys):
    coloredLogger = ColoredLogger(LogLevel.DEBUG)
    coloredLogger.info("What a wonderful info message")
    out, _ = capsys.readouterr()
    assert out == "\033[32m[INFO] What a wonderful info message\033[0m\n"

def test_colored_logger_warn_color(capsys):
    coloredLogger = ColoredLogger(LogLevel.DEBUG)
    coloredLogger.warn("What a wonderful warn message")
    out, _ = capsys.readouterr()
    assert out == "\033[93m[WARN] What a wonderful warn message\033[0m\n"

def test_colored_logger_error_color(capsys):
    coloredLogger = ColoredLogger(LogLevel.DEBUG)
    coloredLogger.error("What a wonderful error message")
    out, _ = capsys.readouterr()
    assert out == "\033[31m[ERROR] What a wonderful error message\033[0m\n"


def test_colored_logger_multiple_logs_with_level_debug(capsys):
    coloredLogger = ColoredLogger(LogLevel.DEBUG)
    coloredLogger.error("What a wonderful error message")
    coloredLogger.info("What a wonderful info message")
    coloredLogger.warn("What a wonderful warn message")
    coloredLogger.debug("What a wonderful debug message")
    out, _ = capsys.readouterr()
    assert out == "\033[31m[ERROR] What a wonderful error message\033[0m\n\033[32m[INFO] What a wonderful info message\033[0m\n\033[93m[WARN] What a wonderful warn message\033[0m\n\033[34m[DEBUG] What a wonderful debug message\033[0m\n"

def test_colored_logger_multiple_logs_with_level_info(capsys):
    coloredLogger = ColoredLogger(LogLevel.INFO)
    coloredLogger.error("What a wonderful error message")
    coloredLogger.info("What a wonderful info message")
    coloredLogger.warn("What a wonderful warn message")
    coloredLogger.debug("What a wonderful debug message")
    out, _ = capsys.readouterr()
    assert out == "\033[31m[ERROR] What a wonderful error message\033[0m\n\033[32m[INFO] What a wonderful info message\033[0m\n\033[93m[WARN] What a wonderful warn message\033[0m\n"

def test_colored_logger_multiple_logs_with_level_warn(capsys):
    coloredLogger = ColoredLogger(LogLevel.WARN)
    coloredLogger.error("What a wonderful error message")
    coloredLogger.info("What a wonderful info message")
    coloredLogger.warn("What a wonderful warn message")
    coloredLogger.debug("What a wonderful debug message")
    out, _ = capsys.readouterr()
    assert out == "\033[31m[ERROR] What a wonderful error message\033[0m\n\033[93m[WARN] What a wonderful warn message\033[0m\n"

def test_colored_logger_multiple_logs_with_level_error(capsys):
    coloredLogger = ColoredLogger(LogLevel.ERROR)
    coloredLogger.error("What a wonderful error message")
    coloredLogger.info("What a wonderful info message")
    coloredLogger.warn("What a wonderful warn message")
    coloredLogger.debug("What a wonderful debug message")
    out, _ = capsys.readouterr()
    assert out == "\033[31m[ERROR] What a wonderful error message\033[0m\n"

def test_time_logger_debug_message(capsys):
    timeLogger = TimeLogger(LogLevel.DEBUG)
    timeLogger.debug("Another debug message")
    t = time.localtime()
    out, _ = capsys.readouterr()
    assert out == f"[{t.tm_hour:>02}:{t.tm_min:>02}:{t.tm_sec:>02}][DEBUG] Another debug message\n"

def test_time_logger_info_message(capsys):
    timeLogger = TimeLogger(LogLevel.DEBUG)
    timeLogger.info("Another info message")
    t = time.localtime()
    out, _ = capsys.readouterr()
    assert out == f"[{t.tm_hour:>02}:{t.tm_min:>02}:{t.tm_sec:>02}][INFO] Another info message\n"

def test_time_logger_warn_message(capsys):
    timeLogger = TimeLogger(LogLevel.WARN)
    timeLogger.warn("Another warn message")
    t = time.localtime()
    out, _ = capsys.readouterr()
    assert out == f"[{t.tm_hour:>02}:{t.tm_min:>02}:{t.tm_sec:>02}][WARN] Another warn message\n"

def test_time_logger_error_message(capsys):
    timeLogger = TimeLogger(LogLevel.DEBUG)
    timeLogger.error("Another error message")
    t = time.localtime()
    out, _ = capsys.readouterr()
    assert out == f"[{t.tm_hour:>02}:{t.tm_min:>02}:{t.tm_sec:>02}][ERROR] Another error message\n"

def test_time_logger_multiple_logs(capsys):
    timeLogger = TimeLogger(LogLevel.DEBUG)
    timeLogger.debug("Another debug message")
    timeLogger.info("Another info message")
    timeLogger.warn("Another warn message")
    timeLogger.error("Another error message")
    t = time.localtime()
    out, _ = capsys.readouterr()
    assert out == f"[{t.tm_hour:>02}:{t.tm_min:>02}:{t.tm_sec:>02}][DEBUG] Another debug message\n[{t.tm_hour:>02}:{t.tm_min:>02}:{t.tm_sec:>02}][INFO] Another info message\n[{t.tm_hour:>02}:{t.tm_min:>02}:{t.tm_sec:>02}][WARN] Another warn message\n[{t.tm_hour:>02}:{t.tm_min:>02}:{t.tm_sec:>02}][ERROR] Another error message\n"

def test_colored_time_logger_debug_message(capsys):
    coloredTimeLogger = ColoredTimeLogger(LogLevel.DEBUG)
    coloredTimeLogger.debug("Another debug message")
    t = time.localtime()
    out, _ = capsys.readouterr()
    assert out == f"\033[34m[{t.tm_hour:>02}:{t.tm_min:>02}:{t.tm_sec:>02}][DEBUG] Another debug message\033[0m\n"

def test_colored_time_logger_info_message(capsys):
    coloredTimeLogger = ColoredTimeLogger(LogLevel.DEBUG)
    coloredTimeLogger.info("Another info message")
    t = time.localtime()
    out, _ = capsys.readouterr()
    assert out == f"\033[32m[{t.tm_hour:>02}:{t.tm_min:>02}:{t.tm_sec:>02}][INFO] Another info message\033[0m\n"

def test_colored_time_logger_warn_message(capsys):
    coloredTimeLogger = ColoredTimeLogger(LogLevel.WARN)
    coloredTimeLogger.warn("Another warn message")
    t = time.localtime()
    out, _ = capsys.readouterr()
    assert out == f"\033[93m[{t.tm_hour:>02}:{t.tm_min:>02}:{t.tm_sec:>02}][WARN] Another warn message\033[0m\n"

def test_colored_time_logger_error_message(capsys):
    coloredTimeLogger = ColoredTimeLogger(LogLevel.DEBUG)
    coloredTimeLogger.error("Another error message")
    t = time.localtime()
    out, _ = capsys.readouterr()
    assert out == f"\033[31m[{t.tm_hour:>02}:{t.tm_min:>02}:{t.tm_sec:>02}][ERROR] Another error message\033[0m\n"

def test_colored_time_logger_multiple_logs(capsys):
    coloredTimeLogger = ColoredTimeLogger(LogLevel.DEBUG)
    coloredTimeLogger.debug("Another debug message")
    coloredTimeLogger.info("Another info message")
    coloredTimeLogger.warn("Another warn message")
    coloredTimeLogger.error("Another error message")
    t = time.localtime()
    out, _ = capsys.readouterr()
    assert out == f"\033[34m[{t.tm_hour:>02}:{t.tm_min:>02}:{t.tm_sec:>02}][DEBUG] Another debug message\033[0m\n\033[32m[{t.tm_hour:>02}:{t.tm_min:>02}:{t.tm_sec:>02}][INFO] Another info message\033[0m\n\033[93m[{t.tm_hour:>02}:{t.tm_min:>02}:{t.tm_sec:>02}][WARN] Another warn message\033[0m\n\033[31m[{t.tm_hour:>02}:{t.tm_min:>02}:{t.tm_sec:>02}][ERROR] Another error message\033[0m\n"

