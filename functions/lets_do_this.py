from output.output import Output
from output.enums import OutputType


def lets_do_this():
    Output().write(message="Here we go!", output_type=OutputType.Log)
    Output().write(message="And there we go!", output_type=OutputType.Log)
    Output().write(message="Test Completed.", output_type=OutputType.Complete)
