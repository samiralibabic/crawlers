# This crawler finds all external links from a specific domain. It visits all internal
# links and extracts external links from those internal pages too.

import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin, urldefrag

internal_links = set()
external_links = set()
visited = set()

def extract_external_links(url):
    global internal_links, external_links

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
    except Exception as e:
        print(f"Error crawling {url}: {e}")
        return

    domain = urlparse(url).netloc

    for link in soup.find_all('a', href=True):
        href = link['href']
        # Remove query parameters and fragments
        href = urldefrag(href)[0].split('?')[0]
        if not is_image_link(href):
            if href.startswith('http'):
                if domain not in href:
                    external_links.add(href)
                else:
                    internal_links.add(href)
            elif href.startswith('/'):
                internal_links.add(urljoin(url, href))

def crawl(url):
    global internal_links, external_links, visited

    visited.add(url)
    queue = [url]

    while queue:
        current_url = queue.pop(0)
        print("Crawling:", current_url)

        extract_external_links(current_url)
        queue.extend(internal_links - visited)
        visited.update(internal_links)

def is_image_link(url):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg']
    for ext in image_extensions:
        if url.lower().endswith(ext):
            return True
    return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python crawler.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    crawl(url)

    print("\nExternal Links:")
    for link in external_links:
        print(link)
