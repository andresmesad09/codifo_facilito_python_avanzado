import csv
import re
from pathlib import Path

FILE_NAME = Path().cwd() / "users.csv"
PATTERN = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?]).{8,}$'

#
# | Part               | Meaning                                              |
# |--------------------|------------------------------------------------------|
# | ^                  | Start of string                                      |
# | (?=.*[a-z])        | Lookahead: at least one lowercase letter anywhere    |
# | (?=.*[A-Z])        | Lookahead: at least one uppercase letter anywhere    |
# | (?=.*\d)           | Lookahead: at least one digit anywhere               |
# | (?=.*[!@#$...])    | Lookahead: at least one symbol from the defined set  |
# | .{8,}              | Any character, 8 or more times (minimum length)      |
# | $                  | End of string                                        |

# What is a lookahead (?=.*X)?
# A lookahead (?=...) is a zero-width assertion — it checks that a condition is true without consuming characters.
# So (?=.*[a-z]) means: 
# "From the current position, somewhere ahead (.*) there must be a lowercase letter — but don't advance the cursor."
# All four lookaheads run from the same starting position (^), independently checking for each character class.
# Only after all pass does .{8,} actually match and consume the full string.


def get_users(file_name: Path) -> list:
    with open(file_name) as f:
        reader = csv.DictReader(f)
        data = list(reader)

    return data


def is_authenticated(username: str, password: str):
    user = {"username": username, "password": password}
    all_users = get_users(FILE_NAME)
    return user in all_users

def is_valid_password(password: str):
    return re.fullmatch(PATTERN, password)
    
    
