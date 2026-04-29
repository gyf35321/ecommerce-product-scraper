# E-commerce Product Data Pipeline

A Python/Selenium-based data pipeline for automated product image collection, structured scraping, and catalog-oriented analysis.

## Overview

E-commerce Product Data Pipeline is an applied automation prototype designed to collect and structure product information from online shopping pages.

The system uses browser automation to extract product-related image data, apply safety limits, remove duplicated or low-value records, and export structured JSON outputs for further catalog analysis.

It is designed as an early-stage sourcing and product intelligence tool for e-commerce research, visual catalog building, and automated product data preparation.

## Key Features

- Browser-based product page automation
- Product image URL extraction
- Controlled scraping with safety limits
- Duplicate filtering and data cleaning
- Structured JSON output generation
- Local image-oriented data organization
- Lightweight pipeline for catalog preparation
- Extensible structure for future product attribute classification

## Tech Stack

- Python
- Selenium
- Requests
- JSON
- Browser automation
- Data cleaning
- Image data collection
- E-commerce data processing

## Project Structure

```text
ecommerce-product-scraper/
├── taobao_scraper.py
├── output_taobao/
│   ├── raw.json
│   ├── cleaned.json
│   └── images/
├── .gitignore
└── README.md