import os
import sys
import re
from urllib.request import urlopen
from urllib.parse import urljoin
from html.parser import HTMLParser

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            href = dict(attrs).get('href')
            if href:
                self.hrefs.append(href)

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_pre = False
        self.pre_content = []

    def handle_starttag(self, tag, attrs):
        if tag == "pre":
            self.in_pre = True
        
    

    def handle_endtag(self, tag):
        if tag == "pre":
            self.in_pre = False

    def handle_data(self, data):
        if self.in_pre:
            self.pre_content.append(data)

def get_linked_pages(url):
    try:
        response = urlopen(url)
        html_content = response.read().decode('utf-8')
        parser = LinkParser()
        parser.feed(html_content)

        # Extract links from the HTML content
        links = [urljoin(url, link) for link in parser.hrefs if not link.startswith("http")]

        return links
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []

def download_and_save_page_content(link, output_folder="output"):
    pre_content = get_pre_content(link)
    if pre_content:
        # Extract the filename from the URL
        filename = os.path.join(output_folder, os.path.basename(link))

        # Write the content to the file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(pre_content)
            print(f"Content from {link} saved to {filename}")

def get_pre_content(url):
    try:
        response = urlopen(url)
        html_content = response.read().decode('utf-8')
        return html_content
        parser = MyHTMLParser()
        parser.feed(html_content)

        return ''.join(parser.pre_content)
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <url>")
        sys.exit(1)

    start_url = sys.argv[1]

    # Create the output folder if it doesn't exist
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)

    # Get linked pages from the provided URL
    linked_pages = get_linked_pages(start_url)

    # Download and save content for each linked page
    for linked_page in linked_pages:
        download_and_save_page_content(linked_page, output_folder)

if __name__ == "__main__":
    main()
