import os
from dotenv import load_dotenv

load_dotenv()
env = os.getenv("ENVIRONMENT")

API_URL = os.getenv(f"{env}_API_URL")
TOKEN = os.getenv(f"{env}_TOKEN")
TEAM_ID = os.getenv(f"{env}_TEAM_ID")
LIST_ID = os.getenv(f"{env}_LIST_ID")