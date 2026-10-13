"""Export the open dataset from the raspberry.tips build output.

Source: content/raspberry-pi-preise-lebenszyklus/tool/data.json + data.csv (built by tool/build.py).
Target: data/prices_lifecycle.json, data/prices.csv, data/lifecycle.csv in this repository.

    python plugins/rpi-prices-lifecycle/scripts/export.py
"""
import csv
import json
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(REPO))
SRC = os.path.join(ROOT, "content", "raspberry-pi-preise-lebenszyklus", "tool")
DATA = os.path.join(REPO, "data")


def main():
    data = json.load(open(os.path.join(SRC, "data.json"), encoding="utf-8"))
    os.makedirs(DATA, exist_ok=True)
    with open(os.path.join(DATA, "prices_lifecycle.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    shutil.copyfile(os.path.join(SRC, "data.csv"), os.path.join(DATA, "prices.csv"))

    cols = ["product_id", "product", "family", "launch_date", "production_until", "status",
            "eol_date", "last_time_buy", "last_time_ship", "verified_primary", "source_url", "checked", "note"]
    with open(os.path.join(DATA, "lifecycle.csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for p in data["products"]:
            eol = p.get("eol") or {}
            src = (p.get("lifecycle_sources") or [{}])[0]
            w.writerow([p["id"], p["name"], p["family"], p.get("launch_date") or "",
                        p.get("production_until") or "", p.get("status") or "",
                        eol.get("eol") or eol.get("eol_date") or "",
                        eol.get("ltb") or eol.get("last_time_buy") or "",
                        eol.get("lts") or eol.get("last_time_ship") or "",
                        str(bool(p.get("verified_primary"))).lower(),
                        src.get("url") or "", p.get("lifecycle_checked") or "", p.get("note") or ""])
    print("products %d, price rows %d" % (len(data["products"]),
          sum(1 for _ in open(os.path.join(DATA, "prices.csv"), encoding="utf-8")) - 1))


if __name__ == "__main__":
    main()
