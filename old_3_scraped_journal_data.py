import os
import json
import pandas as pd
import requests
from bs4 import BeautifulSoup
import logging
from requests.exceptions import RequestException

# ===== INITIAL SETUP =====
OUTPUT_DIR = "3_scraped_journal_data"
os.makedirs(OUTPUT_DIR, exist_ok=True)

JSON_SUCCESS = os.path.join(OUTPUT_DIR, "3_scraped_journal_data.json")
JSON_FAILED = os.path.join(OUTPUT_DIR, "3_scraped_journal_data_failed.json")
LOG_FILE = os.path.join(OUTPUT_DIR, "3_scraped_journal_data.log")
# DATASET_FILE = "2_filtered_journal_data/sample.csv"
DATASET_FILE = "2_filtered_journal_data/2_filtered_journal_data.csv"


# ===== LOGGER SETUP =====
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8"),
    ],
)

logger = logging.getLogger("scraper")


# ===== SCRAPING FUNCTION =====
def extract_dom_structure(body):
    """Ekstrak struktur DOM dari HTML body secara rekursif"""

    def recursive_extract(element):
        if not element:
            return []

        children = [
            {
                "tag": child.name,
                "text": child.get_text(strip=True)[:100],
                "children": recursive_extract(child),
            }
            for child in element.find_all(recursive=False)
            if child.name is not None
        ]
        return children

    return recursive_extract(body)


def scrape_journal(journal_title, journal_url):
    """Melakukan scraping terhadap halaman jurnal dan mengambil struktur DOM dari <body>."""
    try:
        logger.info("=" * 80)
        logger.info(f"Mencoba scraping: {journal_title} | URL: {journal_url}")

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        response = requests.get(journal_url, headers=headers, timeout=15)

        if response.status_code != 200:
            raise RequestException(f"HTTP {response.status_code}")

        soup = BeautifulSoup(response.text, "html.parser")
        body_content = soup.find("body")

        if body_content is None:
            raise ValueError("Tag <body> tidak ditemukan.")

        dom_structure = extract_dom_structure(body_content)
        logger.info(f"✅ Berhasil scraping: {journal_title} | URL: {journal_url}")
        return dom_structure

    except Exception as e:
        logger.error(f"❌ Gagal scraping: {journal_title} | URL: {journal_url} | Error: {e}")
        return None


# ===== MAIN EXECUTION =====
if __name__ == "__main__":
    logger.info("=" * 80)
    logger.info("🚀 Memulai proses scraping jurnal...")
    dataset = pd.read_csv(DATASET_FILE)
    total_journals = len(dataset)
    total_predatory = dataset["is_predatory"].sum()
    total_non_predatory = total_journals - total_predatory

    scraped_data = []
    failed_data = []

    logger.info("=" * 80)
    logger.info(f"📊 Total jurnal yang akan diproses: {total_journals}")
    logger.info(f"   - Jurnal predator: {total_predatory}")
    logger.info(f"   - Jurnal non-predator: {total_non_predatory}")
    logger.info("=" * 80)

    for index, row in dataset.iterrows():
        journal_title = row["journal_title"]
        journal_url = row["journal_url"]
        is_predatory = row["is_predatory"]

        logger.info(f"[{index + 1}/{total_journals}] Scraping: {journal_title}")

        dom_structure = scrape_journal(journal_title, journal_url)

        if dom_structure:
            scraped_data.append({
                "journal_title": journal_title,
                "journal_url": journal_url,
                "is_predatory": is_predatory,
                "dom_structure": dom_structure
            })
        else:
            failed_data.append({
                "journal_title": journal_title,
                "journal_url": journal_url,
                "is_predatory": is_predatory,
                "dom_structure": None
            })

    # Simpan hasil scraping ke JSON
    total_success = len(scraped_data)
    total_failed = len(failed_data)

    if scraped_data:
        with open(JSON_SUCCESS, "w", encoding="utf-8") as json_file:
            json.dump(scraped_data, json_file, indent=4, ensure_ascii=False)
        logger.info(f"📂 Hasil scraping berhasil disimpan: {JSON_SUCCESS} ({total_success} jurnal)")

    if failed_data:
        with open(JSON_FAILED, "w", encoding="utf-8") as json_file:
            json.dump(failed_data, json_file, indent=4, ensure_ascii=False)
        logger.warning(f"⚠️ Data gagal scraping disimpan: {JSON_FAILED} ({total_failed} jurnal)")

    # Analisis hasil
    success_predatory = sum(1 for j in scraped_data if j["is_predatory"])
    success_non_predatory = total_success - success_predatory

    perc_predatory = (success_predatory / total_success * 100) if total_success > 0 else 0
    perc_non_predatory = (success_non_predatory / total_success * 100) if total_success > 0 else 0
    success_rate = (total_success / total_journals * 100) if total_journals > 0 else 0

    logger.info("=" * 80)
    logger.info("🎯 Scraping selesai! Ringkasan hasil:")
    logger.info(f"   ✅ Total berhasil: {total_success} dari {total_journals} ({success_rate:.2f}%)")
    logger.info(f"   ❌ Total gagal: {total_failed} dari {total_journals} ({100 - success_rate:.2f}%)")
    logger.info(f"   🔹 Berhasil (Predator)    : {success_predatory} ({perc_predatory:.2f}%)")
    logger.info(f"   🔹 Berhasil (Non-Predator): {success_non_predatory} ({perc_non_predatory:.2f}%)")
    logger.info("=" * 80)
