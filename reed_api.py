import requests
import os
from dotenv import load_dotenv

load_dotenv()

class ReedAPI:
    def __init__(self):
        self.api_url = "https://www.reed.co.uk/api/1.0/search"
        self.api_key = os.getenv("API_KEY")
        self.api_pass = os.getenv("API_PASS")

    def search_jobs(self, job_title, location):
        """
        Fetch job listings based on the job title and location.
        """
        params = {"keywords": job_title, "locationName": location}
        try:
            response = requests.get(self.api_url, auth=(self.api_key, self.api_pass), params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error while fetching jobs: {e}")
            return {"results": []}
