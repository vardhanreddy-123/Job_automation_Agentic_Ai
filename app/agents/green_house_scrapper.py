from playwright.sync_api import sync_playwright
import json


def scrape_greenhouse_jobs():

    results = []

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        page.goto("https://boards.greenhouse.io/stripe")

        page.wait_for_selector(".Role")

        jobs = page.locator(".Role")

        count = jobs.count()

        print(f"Jobs found: {count}")

        for i in range(count):

            try:

                job = jobs.nth(i)

                title = job.locator("a").inner_text()

                url = job.locator("a").get_attribute("href")

                location = job.locator(".location").inner_text()

                results.append({
                    "title": title,
                    "location": location,
                    "url": url
                })

                print(title)

            except Exception as e:
                print("ERROR:", e)

        browser.close()

    with open("data/greenhouse_jobs.json", "w") as f:
        json.dump(results, f, indent=4)

    print(f"\nSaved {len(results)} jobs")


if __name__ == "__main__":
    scrape_greenhouse_jobs()
