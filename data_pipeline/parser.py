def parse_scheme(page, url):

    container = page.get_by_test_id("desktop-view-container")

    # --------------------------
    # Scheme Name
    # --------------------------

    scheme_name = container.locator("h1").inner_text()

    # --------------------------
    # Ministry
    # --------------------------

    ministry = container.locator("h3").filter(
        has_text="Ministry"
    ).inner_text()

    # --------------------------
    # Description
    # --------------------------

    description = container.locator(
        "#details .markdown-options"
    ).inner_text()

    # --------------------------
    # Benefits
    # --------------------------

    benefits = []

    benefit_items = container.locator(
        "#benefits li"
    )
    eligibility = []

    items = container.locator("#eligibility li")

    for i in range(items.count()):
        eligibility.append(items.nth(i).inner_text())

    for i in range(benefit_items.count()):
        benefits.append(
            benefit_items.nth(i).inner_text()
        )
    exclusions = []

    items = container.locator("#exclusions li")

    for i in range(items.count()):
        exclusions.append(items.nth(i).inner_text())

    application_process = container.locator(
    "#application-process"
    ).inner_text()
    return {

    "name": scheme_name,

    "ministry": ministry,

    "description": description,

    "benefits": benefits,

    "eligibility": eligibility,

    "exclusions": exclusions,

    "application_process": application_process,

    "official_link": url

}