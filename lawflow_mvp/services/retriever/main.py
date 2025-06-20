"""
Retriever module main interface
"""

import logging

logger = logging.getLogger("retriever")
handler = logging.FileHandler("logs/retriever.log")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def run():
    logger.info("Running retriever module logic")
    print("Running retriever module logic")
    return None

if __name__ == "__main__":
    run()
