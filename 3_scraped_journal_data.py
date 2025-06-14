import os
import json
import pandas as pd
import requests
from bs4 import BeautifulSoup
import logging
import random
from requests.exceptions import RequestException
from concurrent.futures import ThreadPoolExecutor, as_completed

# ===== INITIAL SETUP =====
OUTPUT_DIR = "3_scraped_journal_data"
os.makedirs(OUTPUT_DIR, exist_ok=True)

JSON_SUCCESS = os.path.join(OUTPUT_DIR, "3_scraped_journal_data.json")
JSON_FAILED = os.path.join(OUTPUT_DIR, "3_scraped_journal_data_failed.json")
LOG_FILE = os.path.join(OUTPUT_DIR, "3_scraped_journal_data.log")
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

# ===== User-Agent Pool (optional untuk menghindari blokir) =====
USER_AGENTS = [
    # Chrome - Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36",

    # Chrome - macOS
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36",

    # Firefox - Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",

    # Firefox - macOS
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13.5; rv:126.0) Gecko/20100101 Firefox/126.0",

    # Safari - macOS
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",

    # Edge - Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36 Edg/125.0.2535.67",

    # Android - Chrome
    "Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Mobile Safari/537.36",

    # iPhone - Safari
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
]


# ===== SCRAPING UTILITIES =====
def extract_dom_structure(body):
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

def scrape_journal(row):
    journal_title = row["journal_title"]
    journal_url = row["journal_url"]
    is_predatory = row["is_predatory"]

    try:
        headers = {
            "User-Agent": random.choice(USER_AGENTS)
        }

        response = requests.get(journal_url, headers=headers, timeout=15)

        if response.status_code != 200:
            raise RequestException(f"HTTP {response.status_code}")

        soup = BeautifulSoup(response.text, "html.parser")
        body_content = soup.find("body")

        if body_content is None:
            raise ValueError("Tag <body> tidak ditemukan.")

        dom_structure = extract_dom_structure(body_content)

        logger.info(f"✅ {journal_title} | URL: {journal_url}")
        return {
            "journal_title": journal_title,
            "journal_url": journal_url,
            "is_predatory": is_predatory,
            "dom_structure": dom_structure
        }, None

    except Exception as e:
        logger.error(f"❌ {journal_title} | URL: {journal_url} | Error: {e}")
        return None, {
            "journal_title": journal_title,
            "journal_url": journal_url,
            "is_predatory": is_predatory,
            "dom_structure": None
        }

# ===== MAIN EXECUTION =====
if __name__ == "__main__":
    logger.info("=" * 80)
    logger.info("🚀 Memulai proses scraping jurnal secara paralel...")
    dataset = pd.read_csv(DATASET_FILE)
    total_journals = len(dataset)
    total_predatory = dataset["is_predatory"].sum()
    total_non_predatory = total_journals - total_predatory

    logger.info(f"📊 Total jurnal yang akan diproses: {total_journals}")
    logger.info(f"   - Jurnal predator    : {total_predatory}")
    logger.info(f"   - Jurnal non-predator: {total_non_predatory}")
    logger.info("=" * 80)

    scraped_data = []
    failed_data = []

    MAX_WORKERS = 20  # 💡 Bisa disesuaikan dengan kapasitas komputer & koneksi

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [executor.submit(scrape_journal, row) for _, row in dataset.iterrows()]
        for i, future in enumerate(as_completed(futures), start=1):
            result, failed = future.result()
            if result:
                scraped_data.append(result)
            elif failed:
                failed_data.append(failed)

            if i % 100 == 0:
                logger.info(f"💾 Menyimpan sementara: {i} dari {total_journals}")
                with open(JSON_SUCCESS, "w", encoding="utf-8") as json_file:
                    json.dump(scraped_data, json_file, indent=4, ensure_ascii=False)

    # Simpan hasil akhir
    with open(JSON_SUCCESS, "w", encoding="utf-8") as json_file:
        json.dump(scraped_data, json_file, indent=4, ensure_ascii=False)

    with open(JSON_FAILED, "w", encoding="utf-8") as json_file:
        json.dump(failed_data, json_file, indent=4, ensure_ascii=False)

    total_success = len(scraped_data)
    total_failed = len(failed_data)
    success_predatory = sum(1 for j in scraped_data if j["is_predatory"])
    success_non_predatory = total_success - success_predatory

    logger.info("=" * 80)
    logger.info("🎯 Scraping selesai! Ringkasan hasil:")
    logger.info(f"   ✅ Total berhasil      : {total_success} ({(total_success/total_journals)*100:.2f}%)")
    logger.info(f"   ❌ Total gagal         : {total_failed} ({(total_failed/total_journals)*100:.2f}%)")
    logger.info(f"   🔹 Berhasil (Predator) : {success_predatory}")
    logger.info(f"   🔹 Berhasil (Non-Pred) : {success_non_predatory}")
    logger.info("=" * 80)
