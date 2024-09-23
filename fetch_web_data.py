
import requests
from bs4 import BeautifulSoup

def fetch_web_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.get_text()
    else:
        print(f"Failed to fetch data from {url}")
        return None

if __name__ == '__main__':
    url = "https://example.com"
    data = fetch_web_data(url)
    if data:
        print(data)
