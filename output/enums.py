from enum import Enum


class OutputType(Enum):
    """This Enum is used to specify the type of output message being written to the StreamLit status area by the Output
    class. The actual behavior is defined in the frontend code, but comments here describe the intended behavior."""
    Log = 'log'  # A plain line of output is added to the status box
    Error = 'error'  # A line of output is added to the status box visually highlighted as an error
    Status = 'status'  # The active status displayed at the top of the status box is changed to this value
    Complete = 'complete'  # The status box is marked as complete, and the status text is changed to this value
    TerminalError = 'terminal_error'  # The status box is marked as unsuccessfully complete, and the status changed
