# This crawler visits a provided url and extracts eny external links it finds.
# It does not visit internal links nor does it extract external links from them.
import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import os

def get_proxy_settings():
    username = os.environ.get('PYTHONANYWHERE_SITE_NAME')
    if username:
        return {
            'http': f'http://{username}.pythonanywhere.com',
            'https': f'https://{username}.pythonanywhere.com'
        }
    return None

def make_request(url):
    proxy_settings = get_proxy_settings()
    if proxy_settings:
        session = requests.Session()
        session.trust_env = False  # Don't use system proxy settings
        return session.get(url, proxies=proxy_settings)
    else:
        return requests.get(url)

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

def crawl_domain(domain):
    internal_links = set()
    external_links = set()
    visited = set()

    def crawl(url):
        if url in visited:
            return
        visited.add(url)

        try:
            response = make_request(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            for link in soup.find_all('a'):
                href = link.get('href')
                if href:
                    full_url = urljoin(url, href)
                    parsed_url = urlparse(full_url)
                    full_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"

                    if parsed_url.netloc == urlparse(domain).netloc:
                        if full_url not in internal_links and not full_url.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                            internal_links.add(full_url)
                            crawl(full_url)
                    else:
                        external_links.add(full_url)
        except Exception as e:
            print(f"An error occurred while crawling {url}: {e}")

    crawl(domain)
    return list(external_links)

def crawl_url(url):
    try:
        response = make_request(url)
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

