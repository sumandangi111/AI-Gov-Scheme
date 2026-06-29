from playwright.sync_api import sync_playwright
from parser import parse_scheme
from exporter import save_json

def scrape_scheme(url):

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto(url)

        page.wait_for_load_state("networkidle")

        data = parse_scheme(page, url)

        browser.close()

        return data


if __name__ == "__main__":

    url = "https://www.myscheme.gov.in/schemes/pm-kisan"

    scheme = scrape_scheme(url)

    save_json(scheme)

    print(scheme)