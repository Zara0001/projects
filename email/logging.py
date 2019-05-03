# import logging
from logging import getLogger 

logger = logging.getLogger("App")
logger.setLevel(logging.INFO, filemode = "w")

fn = logging.FileHandler("new_log.log")

formatter = logging.Formatter('%(name) - %(levelname) - %(message) - %(asctime)')
fn.setFormatter(formatter)

logger.addHandler(fn)

logger.info("Program started")
logger.info("Done!")
