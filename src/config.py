import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(ENV_PATH)

APP_KEY = os.getenv("KIS_APP_KEY")
APP_SECRET = os.getenv("KIS_APP_SECRET")
KIS_ENV = os.getenv("KIS_ENV", "virtual")

if KIS_ENV == "virtual":
    BASE_URL = "https://openapivts.koreainvestment.com:29443"
else:
    BASE_URL = "https://openapi.koreainvestment.com:9443"


def check_config():
    if not APP_KEY:
        raise ValueError("KIS_APP_KEY가 .env 파일에 없습니다.")

    if not APP_SECRET:
        raise ValueError("KIS_APP_SECRET이 .env 파일에 없습니다.")