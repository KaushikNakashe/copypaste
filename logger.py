import functools
import time
import logging
import colorlog

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console_formatter = colorlog.ColoredFormatter(
    "%(relativeCreated)8dms %(name)10s %(log_color)s%(levelname)s%(reset)s: %(message)s"
)
console.setFormatter(console_formatter)


logger = logging.getLogger("IMPro")
logger.addHandler(console)
logger.setLevel(logging.INFO)


def log_function(func):
    """
    Decorator to log calls to a function with timing info
    """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        logger.info(f'Beginning "{func.__name__}"')
        start_time = time.time()
        ret_val = func(*args, **kwargs)
        duration = time.time() - start_time
        logger.info(f'Completed "{func.__name__}" in {duration:0.2f} seconds')
        return ret_val

    return wrapped_func

