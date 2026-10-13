# Raspberry Pi prices and lifecycle (2012–2026)

Official US list prices of every Raspberry Pi board, Compute Module and Pico since 2012, every announced price
change (including the five memory-driven rounds from October 2025 to October 2026), and the production
guarantees ("will remain in production until at least …") of 45 Raspberry Pi products, each with its primary source.

Interactive version with charts: [https://raspberry.tips/en/raspberrypi-infos/raspberry-pi-prices-lifecycle](https://raspberry.tips/en/raspberrypi-infos/raspberry-pi-prices-lifecycle) · German: [https://raspberry.tips/raspberrypi-infos/raspberry-pi-preisentwicklung-lebenszyklus](https://raspberry.tips/raspberrypi-infos/raspberry-pi-preisentwicklung-lebenszyklus)

## Files

| File | Content |
|---|---|
| `data/prices.csv` | One row per price record: product, date, variant, USD list price, change, event type, basis, source URL |
| `data/lifecycle.csv` | One row per product: launch date, production guarantee, status, EOL / last-time-buy / last-time-ship dates, source |
| `data/prices_lifecycle.json` | Everything above plus price events, the history of extended guarantees, EOL notices, conflicts between official sources and the CPI series used for inflation adjustment |

## Method

- **Sources:** only Raspberry Pi itself — announcements on raspberrypi.com (dated by their `article:published_time`),
  current product briefs from the Product Information Portal (pip.raspberrypi.com), official obsolescence notices,
  and archived copies of official product pages (Internet Archive) for earlier guarantee dates.
- **Prices** are official US list prices in USD, excluding tax and shipping. No shop or marketplace prices.
- **`basis`** says how a price was obtained: `stated` (named in the source), `calculated` (from an announced
  increase, confirmed by a later source where noted), `assumption` (flagged), or change-only rows without an
  absolute price.
- **Conflicts** between official sources are kept, not resolved (e.g. Raspberry Pi 5: product page and brief say
  January 2036, a news post of 17 Sep 2025 says January 2038).
- **Inflation:** US CPI-U (BLS series CUUR0000SA0).

## Citation

Philipp Schweizer, "Raspberry Pi Prices and Lifecycle: Every Model Since 2012", raspberry.tips, October 2026.
See `CITATION.cff`.

## Licence

Data CC BY 4.0, code MIT — see `LICENSE`.
