"""
Intake module main interface
"""

import logging

logger = logging.getLogger("intake")
handler = logging.FileHandler("logs/intake.log")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def run():
    logger.info("Running intake module logic")
    print("Running intake module logic")
    return None

if __name__ == "__main__":
    run()
