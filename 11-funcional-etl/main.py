from extract import extract_user_data
from transform import clean_users
from utils import log_step
from load import save_to_json
from pathlib import Path

FILE_PATH = Path.cwd() / "11-funcional-etl" / "output.json"

@log_step
def run_pipeline():
    raw_data = extract_user_data()
    data = clean_users(raw_data)
    save_to_json(data, FILE_PATH)
    print(data)


if __name__ == "__main__":
    run_pipeline()
