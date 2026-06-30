# from playwright.sync_api import sync_playwright
# from parser import parse_scheme
# from exporter import save_json

# def scrape_scheme(url):

#     with sync_playwright() as p:

#         browser = p.chromium.launch(headless=False)

#         page = browser.new_page()

#         page.goto(url)

#         page.wait_for_load_state("networkidle")

#         data = parse_scheme(page, url)

#         browser.close()

#         return data


# if __name__ == "__main__":

#     url = "https://www.myscheme.gov.in/schemes/pm-kisan"

#     scheme = scrape_scheme(url)

#     save_json(scheme)

#     print(scheme)

from playwright.sync_api import sync_playwright
from parser import parse_scheme
from exporter import save_json
import time
import os


def scrape_scheme(page, url):

    print(f"\nScraping: {url}")

    try:

        page.goto(url, timeout=60000)

        page.wait_for_load_state("networkidle")

        data = parse_scheme(page, url)

        save_json(data)

        print(f"✓ Saved: {data.get('name', 'Unknown Scheme')}")

    except Exception as e:

        print(f"✗ Failed: {url}")

        print(e)


if __name__ == "__main__":

    url_file = "data/urls.txt"

    if not os.path.exists(url_file):

        print("data/urls.txt not found.")
        exit()

    with open(url_file, "r", encoding="utf-8") as file:

        urls = [

            line.strip()

            for line in file

            if line.strip()

        ]

    print("=" * 50)
    print(f"Found {len(urls)} URLs")
    print("=" * 50)

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        for url in urls:

            scrape_scheme(page, url)

            time.sleep(2)

        browser.close()

    print("\n====================================")
    print("Scraping Completed Successfully")
    print("====================================")