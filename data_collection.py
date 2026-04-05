from posixpath import sep
import requests
from datetime import datetime

class data_collector:

    def __init__(self, url, app_id, app_key):
        self.url = url+"/jobs/in/search/"
        self.session = self.build_session(url, app_id, app_key)
        self.pages_scraped = 0
        self.scraped_data = []
    
    def build_session(self, url, app_id, app_key):
        session = requests.Session()
        session.params = {
            "app_id": app_id,
            "app_key": app_key
        }   
        return session
    
    def fetch_results(self, url, page_no):
        try:
            response = self.session.get(self.url+str(page_no))
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            return None
        else: 
            self.pages_scraped += 1
            return response.json()["results"]

    def fetch_data(self, page_no):
        results = self.fetch_results(self.url, page_no)
        if results:
            for job in results:
                self.scraped_data.append({
                    "title": job.get("title"),
                    "company": job.get("company").get("display_name"),
                    "location": job.get("location").get("display_name"),
                    "salary": job.get("salary_min"),
                    "url": job.get("url"),
                    "description": job.get("description"),
                    "created_at": job.get("created_at"),
                    "scraped_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
        else:
            print("No results")