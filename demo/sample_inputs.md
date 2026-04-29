# Sample Inputs — Early-stage Fashion E-commerce Scraping Prototype

## Input context

This project is designed to work with dynamic fashion e-commerce product pages.

The current prototype was originally tested on Taobao-style dynamic product pages, using publicly accessible page resources loaded in the browser.

A typical input context may include:

- public product listing page URL
- public product detail page URL
- target shop or brand page
- dynamically loaded product card elements
- image URLs and visual resources found on the page

## Current extraction focus

The current prototype mainly focuses on extracting and organizing page-level image URLs and visual resources.

The current output is suitable for testing the first stage of a scraping workflow: page access, resource discovery, JSON output generation, and preparation for later filtering.

## Target fields for future enrichment

Future versions may extend the scraper to collect and organize product-level fields such as:

- product title
- brand name
- price
- availability status
- product URL
- image URL
- local image filename
- product category
- cleaned JSON-ready product record

## Current project input/output flow

The current scraper workflow produces:

- `output_taobao/raw.json`
- `output_taobao/cleaned.json`
- downloaded or prepared image assets under `output_taobao/images/`

The current folder name reflects the original Taobao-oriented testing environment. The broader project direction is fashion e-commerce scraping and product-data preparation, with possible future adaptation to luxury marketplace pages such as Farfetch-style public product pages.

This is an independent technical evaluation based on publicly available data, not a collaborative project.