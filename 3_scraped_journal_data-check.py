import os
import logging
import ijson

# ===== SETUP =====
OUTPUT_DIR = "3_scraped_journal_data/check"
DATASET_DIR = "3_scraped_journal_data"
JSON_SUCCESS = os.path.join(DATASET_DIR, "3_scraped_journal_data.json")
JSON_FAILED = os.path.join(DATASET_DIR, "3_scraped_journal_data_failed.json")
LOG_FILE = os.path.join(OUTPUT_DIR, "3_scraped_journal_data_check.log")

# ===== LOGGER SETUP =====
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8"),
    ],
)
logger = logging.getLogger("check")

# ===== STREAMING COUNT FUNCTION =====
def count_entries(filepath, count_predatory=False):
    total = 0
    predatory = 0
    if not os.path.exists(filepath):
        logger.error(f"File tidak ditemukan: {filepath}")
        return 0, 0
    with open(filepath, 'r', encoding='utf-8') as f:
        for item in ijson.items(f, 'item'):
            total += 1
            if count_predatory and item.get("is_predatory") == 1:
                predatory += 1
    return total, predatory

# ===== MAIN CHECK =====
if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    logger.info("=" * 80)
    logger.info("🔍 Memulai pengecekan jumlah data berhasil dan gagal (stream mode)...")

    count_success, pred_success = count_entries(JSON_SUCCESS, count_predatory=True)
    count_failed, _ = count_entries(JSON_FAILED)

    non_pred_success = count_success - pred_success
    total = count_success + count_failed
    percent_success = (count_success / total * 100) if total > 0 else 0
    percent_failed = (count_failed / total * 100) if total > 0 else 0

    logger.info(f"✅ Total berhasil      : {count_success} ({percent_success:.2f}%)")
    logger.info(f"❌ Total gagal         : {count_failed} ({percent_failed:.2f}%)")
    logger.info(f"🔹 Berhasil (Predator) : {pred_success}")
    logger.info(f"🔹 Berhasil (Non-Pred) : {non_pred_success}")
    logger.info(f"📊 Total seluruh data  : {total}")
    logger.info("=" * 80)
