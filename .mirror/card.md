# Raspberry Pi Official Prices and Lifecycle (2012–2026)

Every official **US list price** of Raspberry Pi boards, Compute Modules and Pico since the 2012 launch, including the memory-driven price rounds from October 2025 to November 2026. The dataset also covers the **production guarantees**, end-of-life notices and last-time-buy dates of 45 Raspberry Pi products. Each row links to its primary source.

- **Interactive charts and method:** [raspberry.tips – Raspberry Pi prices and lifecycle](https://raspberry.tips/en/raspberrypi-infos/raspberry-pi-prices-lifecycle) (German: [Raspberry Pi Preisentwicklung und Lebenszyklus](https://raspberry.tips/raspberrypi-infos/raspberry-pi-preisentwicklung-lebenszyklus))
- **Source repository:** [github.com/raspberry-tips/rpi-prices-lifecycle](https://github.com/raspberry-tips/rpi-prices-lifecycle)
- **Citable, versioned archive:** [doi.org/10.5281/zenodo.23336491](https://doi.org/10.5281/zenodo.23336491)

This is a mirror. The GitHub repository is the canonical source and updates first.

## Files

| File | Content |
|---|---|
| `prices.csv` | One row per price record: product, date, variant, USD list price, change, event type, basis, source URL |
| `lifecycle.csv` | One row per product: launch date, production guarantee, status, EOL / last-time-buy / last-time-ship dates, source |
| `prices_lifecycle.json` | Everything above, plus price events, the history of extended guarantees, EOL notices, conflicts between official sources and the CPI series used for inflation adjustment |

## Method

- **Sources:** only Raspberry Pi itself:
  - announcements on raspberrypi.com, dated by their published time
  - product briefs from the Product Information Portal
  - official obsolescence notices
  - archived copies of official product pages
- **Prices** are official US list prices in USD, excluding tax and shipping. No shop or marketplace prices.
- **`basis`** says how each price was obtained:
  - `stated`: named in the source
  - `calculated`: derived from an announced increase
  - `assumption`: flagged as such
- **Conflicts** between official sources are kept, not resolved. For example, for the Raspberry Pi 5 the product brief says January 2036, while a news post says January 2038.
- **Inflation:** US CPI-U (BLS series CUUR0000SA0).

## Citation

Philipp Schweizer, *Raspberry Pi Prices and Lifecycle: Every Model Since 2012*, raspberry.tips. DOI: [10.5281/zenodo.23336491](https://doi.org/10.5281/zenodo.23336491)

## License

Data: CC BY 4.0. Please credit "raspberry.tips" and link to the source. Code in the source repository: MIT.
