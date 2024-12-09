import concurrent.futures
from loguru import logger

from output.output import Output
from output.enums import OutputType


def lets_do_this():
    Output().write(message="Here we go!", output_type=OutputType.Log)
    outputter = Output()
    Output().write(message="Copied the Output() instance...", output_type=OutputType.Log)
    Output().write(message="Here's the multi-threaded part:", output_type=OutputType.Log)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(_do_this, i, outputter) for i in range(2)]
    for future in futures:
        future.result()
    Output().write(message="And there we go!", output_type=OutputType.Log)
    Output().write(message="Test Completed.", output_type=OutputType.Complete)


def _do_this(i, outputter):
    logger.info(f"Doing this {i}...")
    outputter.write(message=f"Doing this {i}...", output_type=OutputType.Log)
