from playwright.sync_api import sync_playwright

url = "https://www.myscheme.gov.in/schemes/pm-kisan"

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto(url)

    page.wait_for_timeout(5000)

    # Save the rendered HTML
    html = page.content()

    with open("pm_kisan.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("HTML Saved Successfully")

    browser.close()