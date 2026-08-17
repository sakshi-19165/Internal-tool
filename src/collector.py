from playwright.async_api import async_playwright


class WebsiteCollector:

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None


    async def start_browser(self):

        self.playwright = await async_playwright().start()

        self.browser = await self.playwright.chromium.launch(
            headless=True
        )

        self.page = await self.browser.new_page(
            viewport={
                "width": 1280,
                "height": 720
            }
        )

        return self.page


    async def open_website(self, url):

        if not self.page:
            raise RuntimeError(
                "Browser has not been started."
            )

        try:

            await self.page.goto(
                url,
                wait_until="domcontentloaded",
                timeout=30000
            )

            # Wait a little for dynamic content
            await self.page.wait_for_timeout(2000)

            return self.page

        except Exception as error:

            raise RuntimeError(
                f"Unable to open website: {error}"
            )


    async def close_browser(self):

        if self.browser:

            await self.browser.close()

        if self.playwright:

            await self.playwright.stop()