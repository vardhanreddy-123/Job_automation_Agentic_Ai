from playwright.sync_api import sync_playwright

def main():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        page.goto("https://jobs.lever.co")

        print("Title:", page.title())

        page.screenshot(path="screenshots/homepage.png")

        input("Press Enter to close...")

        browser.close()

if __name__ == "__main__":
    main()