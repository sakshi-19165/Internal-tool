import json

from pathlib import Path

from datetime import datetime

class ReportExporter:

    def __init__(self):

        self.data_folder = Path(
            "output/data"
        )

        self.report_folder = Path(
            "output/reports"
        )

        self.data_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        self.report_folder.mkdir(
            parents=True,
            exist_ok=True
        )


    def export(
        self,
        research_result
    ):

        company_name = research_result[
            "company_name"
        ]

        safe_name = "".join(
            character
            if character.isalnum()
            else "_"
            for character in company_name.lower()
        )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        # File paths
        json_path = (
            self.data_folder
            /
            f"{safe_name}_{timestamp}.json"
        )

        report_path = (
            self.report_folder
            /
            f"{safe_name}_{timestamp}.md"
        )

        # Create JSON
        self.create_json(
            research_result,
            json_path
        )

        # Create Markdown Report
        self.create_report(
            research_result,
            report_path
        )

        return (
            str(json_path),
            str(report_path)
        )


    def create_json(
        self,
        data,
        file_path
    ):

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )


    def create_report(
        self,
        data,
        file_path
    ):

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                f"# Research Report: "
                f"{data['company_name']}\n\n"
            )

            file.write(
                "## Website\n\n"
            )

            file.write(
                f"{data['website_url']}\n\n"
            )

            file.write(
                "## Research Focus\n\n"
            )

            file.write(
                f"{data['research_focus']}\n\n"
            )

            file.write(
                "## Positioning\n\n"
            )

            file.write(
                f"{data['positioning']}\n\n"
            )

            file.write(
                "## Services\n\n"
            )

            for service in data["services"]:

                file.write(
                    f"- {service}\n"
                )

            file.write("\n")

            file.write(
                "## Main Themes\n\n"
            )

            for theme in data["themes"]:

                file.write(
                    f"- {theme}\n"
                )

            file.write("\n")

            file.write(
                "## Market Signals\n\n"
            )

            for signal in data[
                "market_signals"
            ]:

                file.write(
                    f"- {signal}\n"
                )

            file.write("\n")

            file.write(
                "## Questions for Further Research\n\n"
            )

            for question in data[
                "research_questions"
            ]:

                file.write(
                    f"- {question}\n"
                )