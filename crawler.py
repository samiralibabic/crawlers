# This crawler visits a provided url and extracts eny external links it finds.
# It does not visit internal links nor does it extract external links from them.
import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import os

def make_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def find_external_links(url, domain):
    external_links = set()
    parsed_url = urlparse(url)

    try:
        response = make_request(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                absolute_url = urljoin(url, href)
                parsed_href = urlparse(absolute_url)
                if parsed_href.netloc and parsed_href.netloc != domain and parsed_href.netloc != f"www.{domain}": # Exclude domain and www.domain
                    external_links.add(absolute_url)  # Add the fully qualified external link
    except Exception as e:
        print(f"Error fetching {url}: {e}")

    return external_links

def crawl_domain(url):
    try:
        domain = urlparse(url).netloc
        visited = set()
        to_visit = [url]
        external_links = set()

        while to_visit:
            current_url = to_visit.pop(0)
            if current_url in visited:
                continue

            visited.add(current_url)
            response = requests.get(current_url)
            soup = BeautifulSoup(response.text, 'html.parser')

            for link in soup.find_all('a'):
                href = link.get('href')
                if href:
                    full_url = urljoin(current_url, href)
                    parsed_url = urlparse(full_url)
                    if parsed_url.netloc == domain:
                        if full_url not in visited and full_url not in to_visit:
                            to_visit.append(full_url)
                    else:
                        external_links.add(full_url)

        return list(external_links)
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def crawl_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        base_url = urlparse(url).scheme + "://" + urlparse(url).netloc
        external_links = set()

        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                full_url = urljoin(base_url, href)
                if urlparse(full_url).netloc != urlparse(base_url).netloc:
                    external_links.add(full_url)

        return list(external_links)
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python crawler.py <domain>")
        sys.exit(1)

    input_domain = sys.argv[1]
    domain = input_domain.replace("www.", "")  # Remove "www" prefix if present
    external_links = crawl_domain(domain)
    print(f"\nExternal domains linked from {input_domain}:")
    for external_link in external_links:
        print(external_link)

