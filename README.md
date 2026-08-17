# Automation Project

This project is an internal automation tool designed to collect and extract useful information about companies from the web.

Instead of manually visiting websites and collecting information, the tool automates the process using Python and Playwright. It can collect the available information, process it, and return only the fields that are actually required.

## What Does It Do?

The tool follows a simple workflow:

1. Takes a company name, website, or other supported input.
2. Uses Playwright to access and collect information from the relevant web pages.
3. Parses the collected data.
4. Filters the information based on the user's requirements.
5. Returns the final data in a structured format.

For example, if you only need **company domains or services**, you don't have to collect and use every available data field.

## Features

* Automated data collection using Playwright.
* Extracts and processes relevant company information.
* Supports selective data extraction.
* Reduces manual research and repetitive work.
* Easy to extend with additional fields or scraping logic.

## Tech Stack

* **Python** – Main application logic.
* **Playwright** – Browser automation and web data collection.
* **Parser modules** – Used to clean and extract useful information.
* **Structured output** – Keeps the final results organized and easy to use.

## Project Flow

```text id="pkaq3n"
User Input
    ↓
Scraper
    ↓
Data Collection
    ↓
Parser
    ↓
Filter Required Fields
    ↓
Final Output
```

## Project Structure

```text id="rgdeqw"
project/
│
├── main.py
│   └── Entry point of the application
│
├── scraper/
│   └── Handles Playwright and data collection
│
├── parser/
│   └── Processes and extracts required information
│
├── output/
│   └── Stores generated results
│
├── requirements.txt
│   └── Project dependencies
│
└── README.md
```

## Installation

Clone the repository:

```bash id="lqzo1c"
git clone <repository-url>
cd <project-folder>
```

Install the required Python packages:

```bash id="wlc7ie"
pip install -r requirements.txt
```

Install the required Playwright browsers:

```bash id="wbpf9u"
playwright install
```

## Running the Project

After completing the setup, run:

```bash id="dmvsxm"
python main.py
```

Provide the required input and select the information you want to collect. The tool will handle the collection and processing process and generate the final output.

## Customization

The project is designed to be flexible.

If additional information needs to be collected in the future, new fields or scraping logic can be added without changing the complete project structure. Similarly, the filtering logic can be updated depending on what data the user wants in the final result.

## Purpose

The main purpose of this project is to make company research and data collection faster and more consistent. It focuses on collecting **useful information**, while also giving the flexibility to request only specific data when needed.
