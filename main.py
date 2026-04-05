from dotenv import load_dotenv
import os
from data_collection import data_collector

load_dotenv()
app_id = os.getenv("APP_ID")
app_key = os.getenv("API_KEY")
url = os.getenv("BASE_URL", "https://api.adzuna.com/v1/api")

job_collector = data_collector(url, app_id, app_key)

for page in range(10):
    job_collector.fetch_data(page)
