# Logger

In this exercise you will practice logging, enums and learn more about OOP.

## File tree

```
logger
├── coloredLogger.py
├── coloredTimeLogger.py
├── logLevel.py
├── logger.py
└── timeLogger.py
```

## Help for this exercise

Have a look how to print colored characters on the terminal in Python, as well as time manipulations (see [this link](https://docs.python.org/3/library/time.html)).

Finally, enumerations in Python are explained [here](https://docs.python.org/3/library/enum.html).

## Instructions

### Logger class

This class is the base class for all the loggers you will implement. A logger works with levels: `DEBUG`, `INFO`, `WARN` and `ERROR`. Each of these levels is a measure of importance or severity of a message.

#### LogLevel enum

In the file `logLevel.py`, you have to implement the `LogLevel` enum that contains 4 identifiers `DEBUG`, `INFO`, `WARN` and `ERROR` such that
```
DEBUG < INFO < WARN < ERROR
```
since this enum measures the severity of the message.

#### `__init__`

The rest of the Logger methods are to be implemented in the `logger.py` file.

The `__init__` method takes a level (of type `LogLevel`) as argument, and adds it as an attribute of `self` named `level`.

#### `log`

This method takes two parameters: 
- the level of the log (which is a `LogLevel`)
- the message to be printed (a string)

If the level given in the `log` method is greater or equal than the level of the logger, the message is printed with a trailing newline, else the method does nothing.

The format to print a message is
```
[LEVEL] message
```

with `LEVEL` being the level name (in uppercase) and `message` the message to be printed.

For example, calling `self.log(INFO, "I love this exercise")` prints:
```
[INFO] I love this exercise
```

with a trailing newline (if the logger has level INFO or DEBUG)

#### `debug`

The rest of the `Logger` methods essentially call the `log` method with the good parameters. The `debug` method takes a `message` as argument, passes it to the `log` method with the level `DEBUG`.

#### `info`

This method calls the `log` method with level `INFO` and the message given as argument.

#### `warn`

This method calls the `log` method with level `WARN` and the message given as argument.

#### `error`

This method calls the `log` method with level `ERROR` and the message given as argument.

#### Testing

You should test your logger to see if everything works fine. For instance, the following code:

```python
logger = Logger(LogLevel.WARN)
logger.info("this is an info message")
logger.error("this is an error message")
logger.debug("this is a debug message")
logger.warn("this is a warn message")
```

produces the following output:
```
[ERROR] this is an error message
[WARN] this is a warn message
```

### ColoredLogger

This class is derived from the Logger class. To make this class work, you only have to override the `__init__` method and the `log` method.

#### `__init__`

The `__init__` should only call the parent `__init__` method with the same argument.

#### `log`

The format of the messages is left unchanged, but the color is different: 

- DEBUG messages should be printed in blue (ANSI code 34)
- INFO messages should be printed in green (ANSI code 32)
- WARN messages should be printed in yellow (ANSI code 93)
- ERROR messages should be printed in red (ANSI code 31)

---
*Tip!*

Don't forget to reset the color at the end of the logs.

---

### TimeLogger

This class is derived from the Logger class. To make this class work, you only have to override the `__init__` method and the `log` method.

#### `__init__`

The `__init__` method should only call the parent `__init__` method with the same argument.

#### `log`

The format of the message is changed, and looks like this
```
[LEVEL][HH:MM:SS] message
```

For instance, if the local time is Thursday July 18, 2024 at 2:07:40 PM, and `log` is called with parameters `ERROR` and `This is an error message`, the output is
```
[ERROR][14:07:40] This is an error message
```

### ColoredTimeLogger

This class is derived from **ColoredLogger** and **TimeLogger**, and you have to override the `__init__` and `log` methods.

#### `__init__`

This method should call one of the parents' `__init__` method with the same argument.

#### `log`

This methods combines the two `log` methods of the parent classes. It displays the local time in the output and the output is colored the same way as it would be with the `ColoredLogger`.
