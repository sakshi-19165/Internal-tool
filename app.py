import asyncio

from src.collector import WebsiteCollector
from src.parser import WebsiteParser
from src.analyzer import ResearchAnalyzer
from src.exporter import ReportExporter
from src.utils import validate_url, setup_logger


async def main():

    logger = setup_logger()

    print("\n===== COMPETITOR RESEARCH TOOL =====\n")

    company_name = input(
        "Enter company name: "
    ).strip()

    website_url = input(
        "Enter website URL: "
    ).strip()

    research_focus = input(
        "What do you want to research? "
    ).strip()


    # -------------------------
    # VALIDATE URL
    # -------------------------

    try:

        validate_url(website_url)

    except ValueError as error:

        print(f"\nInvalid URL: {error}")

        return


    collector = WebsiteCollector()


    try:

        # -------------------------
        # STEP 1: START BROWSER
        # -------------------------

        print(
            "\n[1/4] Opening browser..."
        )

        await collector.start_browser()


        # -------------------------
        # STEP 2: OPEN WEBSITE
        # -------------------------

        print(
            "[2/4] Collecting website..."
        )

        page = await collector.open_website(
            website_url
        )


        # -------------------------
        # STEP 3: PARSE WEBSITE
        # -------------------------

        print(
            "[3/4] Extracting website information..."
        )

        parser = WebsiteParser()

        website_data = await parser.parse(
            page,
            website_url
        )


        # -------------------------
        # STEP 4: ANALYZE
        # -------------------------

        print(
            "[4/4] Analyzing information..."
        )

        analyzer = ResearchAnalyzer()

        research_result = analyzer.analyze(

            company_name=company_name,

            website_data=website_data,

            research_focus=research_focus
        )


        # -------------------------
        # EXPORT
        # -------------------------

        exporter = ReportExporter()

        json_path, report_path = exporter.export(
            research_result
        )


        print(
            "\n===== RESEARCH COMPLETED ====="
        )

        print(
            f"\nJSON saved to:\n{json_path}"
        )

        print(
            f"\nReport saved to:\n{report_path}"
        )


    except Exception as error:

        print(
            f"\nSomething went wrong: {error}"
        )

        logger.exception(
            f"Tool failed: {error}"
        )


    finally:

        await collector.close_browser()


if __name__ == "__main__":

    asyncio.run(main())