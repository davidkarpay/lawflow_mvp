"""
Clarifier module main interface
"""

import logging

logger = logging.getLogger("clarifier")
handler = logging.FileHandler("logs/clarifier.log")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def run():
    logger.info("Running clarifier module logic")
    print("Running clarifier module logic")
    return None

if __name__ == "__main__":
    run()
