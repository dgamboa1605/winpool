import datetime
import logging
import os


class Logger:
    """
    Wraps Logger methods for logging messages at different levels,
    also provides methods for logging method entry and exit.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes the LoggerManager and configures the logger.
        The log messages will be written to a log file with a timestamp in the name.
        """
        self._create_logs_folder()
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(lineno)d - %(message)s")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
        filename = f"logs/logs_{timestamp}.log"

        file_handler = logging.FileHandler(filename)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def _create_logs_folder(self) -> None:
        """
        Creates the 'logs' folder if it doesn't exist.
        """
        logs_folder = 'logs'
        if not os.path.exists(logs_folder):
            os.makedirs(logs_folder)

    def debug(self, message) -> None:
        """
        Writes a log message at the debug level.
        Args:
            message (str): The log message.
        """
        self.logger.debug(message)

    def info(self, message) -> None:
        """
        Writes a log message at the info level.
        Args:
            message (str): The log message.
        """
        self.logger.info(message)

    def warning(self, message) -> None:
        """
        Writes a log message at the warning level.
        Args:
            message (str): The log message.
        """
        self.logger.warning(message)

    def error(self, message) -> None:
        """
        Writes a log message at the error level.
        Args:
            message (str): The log message.
        """
        self.logger.error(message)

    def critical(self, message) -> None:
        """
        Writes a log message at the critical level.
        Args:
            message (str): The log message.
        """
        self.logger.critical(message)
