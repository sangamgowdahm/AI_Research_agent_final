
from dotenv import load_dotenv
load_dotenv()

import requests
import os

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

def test_tavily_api():
    query = "latest AI research papers"
    url = "https://api.tavily.com/search"
    
    payload = {
        "api_key": TAVILY_API_KEY,
        "query": query,
        "num_results": 3
    }

    response = requests.post(url, json=payload)  # ✅ Use POST request

    if response.status_code == 200:
        print("Tavily API Response:", response.json())
    else:
        print(f"Error: {response.status_code}, Response: {response.text}")

test_tavily_api()
