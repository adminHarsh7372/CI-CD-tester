import requests
from bs4 import BeautifulSoup

def scrape_example():
    url = "http://example.com"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find("h1").text
        print(f"Page title: {title}")
    else:
        print(f"Failed to fetch page, status code: {response.status_code}")

if __name__ == "__main__":
    scrape_example()
