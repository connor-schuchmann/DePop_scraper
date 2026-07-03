# Legacy: Depop scraping attempt

This folder holds the original approach to this project: scraping Depop's
search results directly.

- `check_depop.py` — plain `requests` call with a spoofed browser User-Agent.
  Depop returns a page that doesn't contain listing data without JS, and
  spoofing headers to get around that is the kind of thing that crosses into
  ToS-violating territory.
- `check.py` — Playwright-driven browser scraping (scroll + wait + dump full
  page HTML). This got further, but running an automated browser against
  Depop's live site to systematically extract listings is still scraping,
  and Depop's ToS prohibits automated data collection.
- `parse_depop.py` — BeautifulSoup parser for the HTML dumped by `check.py`.
- `listings.json` / `api_listings_raw.json` / `depop_raw.html` — sample
  output from the above, kept only as a record of what the scrape produced.

**Why this was abandoned:** hitting real anti-bot defenses made clear this
wasn't a sound long-term approach, and it isn't worth the ToS risk for a
learning/resume project. The project moved to eBay's official Browse API
instead (see the top-level `ebay_client.py` and root `README.md`), which
provides the same kind of data through a supported, authenticated channel.

`analysis.py` (the deal-finder logic) didn't need to change — it just reads
a `listings.json` with `brand`/`size`/`price`/`url` fields, regardless of
where that file came from.

To run this old code, install `legacy/requirements.txt` instead of the
top-level one.
