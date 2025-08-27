import os
import sys
import logging

##custom logger string
logging_str ="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

##loggidirectory name: log
log_dir_name="logs"

##loggig file name : log_history.log
log_filepath = os.path.join(log_dir_name, "log_history.log")

##create the directory
os.makedirs(log_dir_name, exist_ok=True)

##handler setup

logging.basicConfig(
    level= logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger=logging.getLogger("cnnClassifierLogger")