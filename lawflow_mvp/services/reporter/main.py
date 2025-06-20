"""
Reporter module main interface
"""

import logging

logger = logging.getLogger("reporter")
handler = logging.FileHandler("logs/reporter.log")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def run():
    logger.info("Running reporter module logic")
    print("Running reporter module logic")
    return None

if __name__ == "__main__":
    run()
