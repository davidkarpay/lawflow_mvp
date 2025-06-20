"""
Query_builder module main interface
"""

import logging

logger = logging.getLogger("query_builder")
handler = logging.FileHandler("logs/query_builder.log")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def run():
    logger.info("Running query_builder module logic")
    print("Running query_builder module logic")
    return None

if __name__ == "__main__":
    run()
