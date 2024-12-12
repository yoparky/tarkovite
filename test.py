import requests
from bs4 import BeautifulSoup
import pandas as pd

# Fetch webpage
url = "https://smoothstack.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
}
response = requests.get(url, headers=headers)
if response.status_code!= 200:
    print(f"Error fetching webpage: {response.status_code}")
    exit()

print(response)
print(response.content)