import time


def log_step(func: callable):
    def wrapper(*args, **kwargs):
        print(f"\n[LOG] Running: {func.__name__}")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"\n[LOG] Completed: {func.__name__} in {end - start:.6f} ")
        return result

    return wrapper
