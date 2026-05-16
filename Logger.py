import os, logging
from datetime import datetime
from glob import glob
from functools import wraps

# Logger
def log():
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    path = "logs/*.log"
    files = glob(path)
    if len(files) >= 5:
        os.remove(files[0])


    date_now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".log"
    log_path = os.path.join(log_dir, date_now)
    logging.basicConfig(level = logging.DEBUG, filename = log_path, filemode = "w", format = "%(asctime)s - %(levelname)s - %(message)s")
    logger = logging.getLogger("Logger")
    logger.debug("Initializing logger")
    return logger

# Global variables:
logger = log()

# Decorators:
def dlog(message = ""):
    def dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            name = func.__name__
            logger.debug(f"def {name} - invocation")
            try:
                if message != "":
                    logger.debug(f"def {name} - {message}")
                res = func(*args, **kwargs)
                return res
            except Exception:
                logger.exception(f"At {name} occurred some unexpected error")
        return wrapper
    return dec