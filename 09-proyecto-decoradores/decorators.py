import functools
from utils import is_authenticated, is_valid_password


def authenticate_class(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if is_authenticated(*args, **kwargs):
            return cls(*args, **kwargs)
        else:
            raise Exception("Unauthorized user")

    return wrapper

def validate_password(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        pwd = args[0].password
        if is_valid_password(pwd):
            return func(*args, **kwargs)
        else:
            raise Warning("Ojito con la password, pirocheche")
    return wrapper
