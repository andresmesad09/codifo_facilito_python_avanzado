import logging
from threading import Thread, Lock

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

logger.addHandler(console_handler)

ITERATIONS = 1_000_000

class BankFacilito:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for _ in range(ITERATIONS):
            with self.lock:
                self.balance += 1

    def withdraw(self):
        for _ in range(ITERATIONS):
            with self.lock:
                self.balance -= 1

for run in range(5):
    bank = BankFacilito()
    t1 = Thread(target=bank.deposit)
    t2 = Thread(target=bank.withdraw)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    logger.info(f"Run {run + 1} | expected=0 | actual={bank.balance}")