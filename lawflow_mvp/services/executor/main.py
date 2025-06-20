"""
Executor module main interface
"""

import logging

logger = logging.getLogger("executor")
handler = logging.FileHandler("logs/executor.log")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def run():
    logger.info("Running executor module logic")
    print("Running executor module logic")
    return None

if __name__ == "__main__":
    run()
