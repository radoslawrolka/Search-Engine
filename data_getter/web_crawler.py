import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from collections import deque


def get_data(config):
    counter = 0
    queue = deque([config["START_CRAWL"]])
    visited = set()

    while queue and counter < config["MAX_PAGES"]:
        page = queue.popleft()
        if page in visited:
            continue
        visited.add(page)
        counter += 1
        print(f"Fetching {page} ...{counter}/{config['MAX_PAGES']}")
        response = requests.get(urljoin(config["DOMAIN"], page))
        soup = BeautifulSoup(response.text, "html.parser")

        with open(f"./wiki/{page}.txt", "w") as f:
            for tag in soup.find_all(["h1", "h2", "h3", "h4", "h5", "p"]):
                f.write(tag.get_text() + "\n")

        for anchor in soup.select("#bodyContent a"):
            href = anchor.get("href")
            if href and href.startswith("/wiki/") and ":" not in href:
                queue.append(href[6:])
