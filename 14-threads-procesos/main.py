import requests
import time
from threading import Thread
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    fmt="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# File handler
file_handler = logging.FileHandler("app.log", mode="a")
file_handler.setLevel(logging.WARNING)  # only WARNING and above to file
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

API_URL = "https://randomuser.me/api/"


def get_user(x):
    response = requests.get(API_URL)
    if response.status_code == 200:
        logger.info(f"Success - Thread {x}")
    else:
        logger.error(f"Error - Thread {x}")


start = time.time()
threads = []
for x in range(100):
    thread = Thread(target=get_user, name=x, kwargs={'x': x})
    thread.start()
    threads.append(thread)

for t in threads:
    t.join()
logger.info(f"Execution time: {time.time() - start}")
