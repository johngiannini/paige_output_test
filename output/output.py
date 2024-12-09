from loguru import logger

from structure.singleton_meta import SingletonMeta
from output.enums import OutputType


class Output(metaclass=SingletonMeta):
    def __init__(self):
        self.verbose = True
        self.on_log = None
        self.on_error = None
        self.on_status = None
        self.on_complete = None
        self.on_terminal_error = None

    def configure(self, on_log, on_error, on_status, on_complete, on_terminal_error, verbose=True):
        self.on_log = on_log
        self.on_error = on_error
        self.on_status = on_status
        self.on_complete = on_complete
        self.verbose = verbose
        self.on_terminal_error = on_terminal_error

    def write(self, message, output_type):
        if self.verbose and output_type == OutputType.Log:
            if self.on_log:
                self.on_log(message)
            else:
                logger.info(message)
        elif output_type == OutputType.Error:
            if self.on_error:
                self.on_error(message)
            else:
                logger.error(message)
        elif output_type == OutputType.Status:
            if self.on_status:
                self.on_status(message)
            else:
                logger.info(f"status changed to: {message}")
        elif output_type == OutputType.Complete:
            if self.on_complete:
                self.on_complete(message)
            else:
                logger.info(f"task completed: {message}")
        elif output_type == OutputType.TerminalError:
            if self.on_terminal_error:
                self.on_terminal_error(message)
            else:
                logger.error(f"task failed: {message}")