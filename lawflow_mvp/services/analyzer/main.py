"""
Analyzer module main interface
"""

import logging

logger = logging.getLogger("analyzer")
handler = logging.FileHandler("logs/analyzer.log")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def run():
    logger.info("Running analyzer module logic")
    print("Running analyzer module logic")
    return None

if __name__ == "__main__":
    run()
