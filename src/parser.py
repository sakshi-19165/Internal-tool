class WebsiteParser:

    async def parse(self, page, url):

        # -------------------------
        # TITLE
        # -------------------------

        try:

            title = await page.title()

        except Exception:

            title = ""


        # -------------------------
        # META DESCRIPTION
        # -------------------------

        try:

            meta_description = await page.locator(
                'meta[name="description"]'
            ).get_attribute("content")

            if not meta_description:
                meta_description = ""

        except Exception:

            meta_description = ""


        # -------------------------
        # HEADINGS
        # -------------------------

        headings = []

        heading_elements = page.locator(
            "h1, h2, h3"
        )

        heading_count = await heading_elements.count()

        for index in range(heading_count):

            try:

                text = await heading_elements.nth(
                    index
                ).inner_text()

                text = text.strip()

                if text:

                    headings.append(text)

            except Exception:

                continue


        # -------------------------
        # PARAGRAPHS
        # -------------------------

        paragraphs = []

        paragraph_elements = page.locator("p")

        paragraph_count = await paragraph_elements.count()

        for index in range(paragraph_count):

            try:

                text = await paragraph_elements.nth(
                    index
                ).inner_text()

                text = text.strip()

                # Ignore very small text
                if len(text) > 30:

                    paragraphs.append(text)

            except Exception:

                continue


        # -------------------------
        # LINKS
        # -------------------------

        links = []

        link_elements = page.locator("a")

        link_count = await link_elements.count()

        for index in range(link_count):

            try:

                text = await link_elements.nth(
                    index
                ).inner_text()

                href = await link_elements.nth(
                    index
                ).get_attribute("href")

                if text and href:

                    links.append({

                        "text": text.strip(),

                        "url": href
                    })

            except Exception:

                continue


        # -------------------------
        # REMOVE DUPLICATES
        # -------------------------

        headings = list(
            dict.fromkeys(headings)
        )

        paragraphs = list(
            dict.fromkeys(paragraphs)
        )


        # -------------------------
        # RETURN DATA
        # -------------------------

        return {

            "url": url,

            "title": title,

            "meta_description":
                meta_description,

            "headings":
                headings,

            "paragraphs":
                paragraphs,

            "links":
                links
        }