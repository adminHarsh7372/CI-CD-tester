import requests
from bs4 import BeautifulSoup

def main():
    url = "https://quotes.toscrape.com/"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch page: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.select(".quote span.text")
    authors = soup.select(".quote small.author")

    for quote, author in zip(quotes[:5], authors[:5]):
        print(f"{quote.text} — {author.text}")

if __name__ == "__main__":
    main()
