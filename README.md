# Resale deal finder

Learning/resume project: pull secondhand clothing listings for a search term
and flag the ones priced well below the average (mean − 1 std dev).

## Status

Originally built against Depop by scraping search-result HTML. That hit
anti-bot defenses fast, and scraping a marketplace's live site isn't a great
foundation for a project meant to demonstrate good practice anyway — see
[`legacy/README.md`](legacy/README.md) for what was tried and why it was
dropped.

Now rebuilt on **eBay's official Browse API** (OAuth client-credentials
flow, no scraping). Currently waiting on eBay developer API keys; once those
land, drop them into `.env` (see `.env.example`) and it's ready to run.

## Usage (once EBAY_CLIENT_ID / EBAY_CLIENT_SECRET are set in `.env`)

```
pip install -r requirements.txt
python ebay_client.py "volcom shorts" --limit 50
python analysis.py
```

`ebay_client.py` writes `listings.json` in the schema `analysis.py` expects
(`brand`, `size`, `price`, `url`), so `analysis.py` needed no changes when
the data source changed.
