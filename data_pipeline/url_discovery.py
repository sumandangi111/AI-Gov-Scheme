from playwright.sync_api import sync_playwright
import json
import os


def discover_scheme_urls():

    urls = set()

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto("https://www.myscheme.gov.in/search")

        page.wait_for_load_state("networkidle")

        # -----------------------------
        # Collect Scheme URLs
        # -----------------------------
        scheme_links = page.locator("a[href*='/schemes/']")

        for i in range(scheme_links.count()):

            href = scheme_links.nth(i).get_attribute("href")

            if href:

                if href.startswith("/"):
                    href = "https://www.myscheme.gov.in" + href

                urls.add(href)

        print(f"\nCollected Scheme URLs: {len(urls)}")

        # -----------------------------
        # DEBUG ALL LINKS
        # -----------------------------
        print("\n========== ALL LINKS ==========\n")

        links = page.locator("a")

        print("Total Links:", links.count())

        for i in range(links.count()):

            try:
                text = links.nth(i).inner_text().strip()
                href = links.nth(i).get_attribute("href")

                print(f"Link {i}")
                print("TEXT :", text)
                print("HREF :", href)
                print("-" * 60)

            except Exception:
                pass

        browser.close()

    return sorted(urls)


if __name__ == "__main__":

    urls = discover_scheme_urls()

    os.makedirs("data", exist_ok=True)

    with open("data/urls.txt", "w", encoding="utf-8") as f:
        for url in urls:
            f.write(url + "\n")

    with open("data/urls.json", "w", encoding="utf-8") as f:
        json.dump(urls, f, indent=4)

    print("\n==============================")
    print("Total URLs:", len(urls))
    print("==============================")