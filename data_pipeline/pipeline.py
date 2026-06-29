from scraper import scrape_scheme
from exporter import save_json
from urls import URLS


def run_pipeline():

    for url in URLS:

        print("=" * 60)
        print("Scraping:", url)

        try:

            scheme = scrape_scheme(url)

            save_json(scheme)

            print("Success")

        except Exception as e:

            print("Failed:", e)


if __name__ == "__main__":

    run_pipeline()