"""Module for scraping job postings from Lever."""

# pylint: disable=duplicate-code

import json

from playwright.sync_api import sync_playwright


def scrape_jobs():
    """Scrapes Lever jobs and saves them to a JSON file."""
    results = []

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        page.goto("https://boards.greenhouse.io/stripe")

        page.wait_for_timeout(5000)

        jobs = page.locator(".posting")

        count = jobs.count()

        print(f"Jobs found: {count}")

        for i in range(count):

            try:

                job = jobs.nth(i)

                title = job.locator(".posting-title h5").inner_text()

                location = job.locator(".posting-categories .sort-by-location").inner_text()

                link = job.get_attribute("href")

                results.append({
                    "title": title,
                    "location": location,
                    "url": link
                })

                print(title)

            except Exception as e:  # pylint: disable=broad-exception-caught
                print("Error:", e)

        browser.close()

    with open("data/jobs.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)

    print(f"\nSaved {len(results)} jobs")


if __name__ == "__main__":
    scrape_jobs()
