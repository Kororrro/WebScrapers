import time
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "ResearchBot/1.0 (contact: you@example.com)"
}
for i in range(1,6):
    url = f"https://useme.com/pl/jobs/category/programowanie-i-it,35/?page={i}"
    print(url)

    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")

    for article in soup.select("article"):
        title = article.get_text(strip=True)
        print(title)

    time.sleep(5)  # conservative pacing