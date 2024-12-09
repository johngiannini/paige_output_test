import concurrent.futures
from loguru import logger
from queue import Queue
import time

from output.output import Output
from output.enums import OutputType


def lets_do_this(sc):
    Output().write(message="Here we go!", output_type=OutputType.Log)
    output_queue = Queue()

    Output().write(message="Here's the multi-threaded part:", output_type=OutputType.Log)
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Here futures is a dictionary, rather than a list as we'd been using previously
        futures = {executor.submit(_do_this, i, output_queue): i for i in range(5)}

        while futures:
            while not output_queue.empty():  # Each time we loop, watch the Queue for output and print anything there
                Output().write(message=output_queue.get(), output_type=OutputType.Log)

            # Check for completed futures, but don't wait for them too long (0.1 seconds)
            done, _ = concurrent.futures.wait(futures, timeout=0.1, return_when=concurrent.futures.FIRST_COMPLETED)
            # Process any futures that are completed and remove them from futures (or the outer while loop will never end)
            for future in done:
                task_id = futures[future]
                result = future.result()  # Retrieve the result
                Output().write(message=f"Task {task_id} finished with result: {result}", output_type=OutputType.Log)
                del futures[future]



    Output().write(message="And there we go!", output_type=OutputType.Log)
    Output().write(message="Test Completed.", output_type=OutputType.Complete)


def _do_this(i, output_queue):
    logger.info("Doing this {i}...")
    output_queue.put(f"Doing this {i} first time...")
    time.sleep(2)
    output_queue.put(f"Doing this {i} second time...")
    time.sleep(2)
    output_queue.put(f"Doing this {i} third time...")
    logger.info("Done with this {i}.")
    return i