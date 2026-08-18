import os
import logging
from datetime import datetime

class LoggerService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LoggerService, cls).__new__(cls)
            cls._instance._setup_logger()
        return cls._instance

    def _setup_logger(self):
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        self.logger = logging.getLogger("SuitFavicon")
        self.logger.setLevel(logging.DEBUG)

        # File Handler (Audit)
        audit_file = os.path.join(log_dir, "audit.log")
        fh = logging.FileHandler(audit_file, encoding='utf-8')
        fh.setLevel(logging.DEBUG)

        # Formatter
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(module_name)s | %(message)s')
        fh.setFormatter(formatter)

        self.logger.addHandler(fh)

    def log_event(self, module, event, state="OK"):
        """
        Logs a standardized event: date | module | event | state
        """
        message = f"{event} | {state}"
        self.logger.info(message, extra={'module_name': module})

    def log_error(self, module, error_msg, stack_trace=None):
        """
        Logs an error with stack trace if provided.
        """
        message = f"ERROR: {error_msg}"
        if stack_trace:
            message += f"\nSTACK: {stack_trace}"
        self.logger.error(message, extra={'module_name': module})

    @staticmethod
    def get_logger():
        return LoggerService().logger
