class ResearchAnalyzer:

    def analyze(
        self,
        company_name,
        website_data,
        research_focus
    ):

        headings = website_data.get(
            "headings",
            []
        )

        paragraphs = website_data.get(
            "paragraphs",
            []
        )

        meta_description = website_data.get(
            "meta_description",
            ""
        )

        # --------------------------
        # COMPANY POSITIONING
        # --------------------------

        positioning = (
            meta_description
            if meta_description
            else "No clear positioning found."
        )

        # --------------------------
        # SERVICES
        # --------------------------

        service_keywords = [

            "service",
            "services",
            "course",
            "courses",
            "consulting",
            "development",
            "design",
            "research",
            "solution",
            "solutions",
            "training"
        ]

        services = []

        for heading in headings:

            heading_lower = heading.lower()

            if any(
                keyword in heading_lower
                for keyword in service_keywords
            ):

                services.append(
                    heading
                )

        if not services:

            services = headings[:5]

        # --------------------------
        # MAIN THEMES
        # --------------------------

        themes = headings[:10]

        # --------------------------
        # MARKET SIGNALS
        # --------------------------

        signal_keywords = [

            "client",
            "customer",
            "partner",
            "case study",
            "award",
            "team",
            "growth",
            "global"
        ]

        market_signals = []

        for paragraph in paragraphs:

            paragraph_lower = paragraph.lower()

            if any(
                keyword in paragraph_lower
                for keyword in signal_keywords
            ):

                market_signals.append(
                    paragraph
                )

        # --------------------------
        # RESEARCH QUESTIONS
        # --------------------------

        research_questions = [

            f"What problem does {company_name} solve?",

            "Who is the main target audience?",

            "What services appear to be most important?",

            "What makes this company different?",

            f"How does the website support the research focus: {research_focus}?"
        ]

        # --------------------------
        # FINAL RESULT
        # --------------------------

        return {

            "company_name":
                company_name,

            "website_url":
                website_data["url"],

            "research_focus":
                research_focus,

            "positioning":
                positioning,

            "services":
                services,

            "themes":
                themes,

            "market_signals":
                market_signals,

            "research_questions":
                research_questions
        }