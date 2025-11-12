# Scraper CI

A simple Scrapy-based web scraper that extracts quotes, authors, and tags from Quotes to Scrape
 and outputs them as a CSV file. Designed to run as a standalone Python script and fully compatible with GitHub Actions CI/CD pipelines.

# Features

Scrapes quotes, authors, and tags from the first 5 pages.

Outputs data in CSV format (output/quotes.csv).

Fully automated workflow using GitHub Actions.

Artifact storage for easy download of scraped data.

File Structure
.
├─ quotes_spider.py   # The Scrapy spider
├─ main.py            # Standalone runner (outputs CSV)
├─ requirements.txt   # Project dependencies
├─ .github/
      └─ workflows/
        └─ ci.yml   # GitHub Actions workflow


Installation

# Clone the repository

git clone https://github.com/adminHarsh7372/CI-CD-tester.git


# Install dependencies

pip install -r requirements.txt


# GitHub Actions CI/CD

The workflow automatically runs the spider in 3 stages: setup, scrape, validate.

The CSV output is stored as an artifact for download from the workflow run.


# Notes

The spider scrapes only the first 5 pages to avoid long runtimes.

CSV output will have columns: text, author, tags.
