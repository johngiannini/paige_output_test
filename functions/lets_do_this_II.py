import concurrent.futures
from loguru import logger
import streamlit as st


def lets_do_this(sc):
    sc.write("Here we go!")
    sc.write("Here's the multi-threaded part:")
    # with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    #     futures = [executor.submit(_do_this, i, sc) for i in range(2)]
    # for future in futures:
    #     future.result()
    sc.write("And there we go!")
    sc.update(label="Test Completed.", state="complete", expanded=False)


def _do_this(i, sc):
    logger.info(f"Doing this {i}...")
    sc.write(f"Doing this {i}...")