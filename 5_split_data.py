import json
import os
import logging
from sklearn.model_selection import train_test_split

LOG_DIR = "5_split_data"
LOG_FILE = os.path.join(LOG_DIR, "5_split_data.log")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ],
)

INPUT_DIR = "4_preprocess_scraped_data"
OUTPUT_DIR = "5_split_data"

FILES = {
    "bfs": "4_bfs_preprocess_scraped_data.json",
    "dfs": "4_dfs_preprocess_scraped_data.json"
}

# Rasio pembagian data
TRAIN_RATIO = 0.8

def load_data(filepath):
    """Membaca dataset dari file JSON dan menghitung total entri."""
    logging.info(f"Memuat data dari {filepath}...")
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    total_entries = len(data)
    total_predatory = sum(1 for entry in data if entry["is_predatory"] == 1)
    total_non_predatory = total_entries - total_predatory

    logging.info(f"Total data dalam {filepath}: {total_entries} entri")
    logging.info(f"  - Jurnal predator: {total_predatory}")
    logging.info(f"  - Jurnal non-predator: {total_non_predatory}")

    return data, total_predatory, total_non_predatory

def split_and_save(data, filename_prefix):
    """Membagi dataset menjadi train-test dengan stratifikasi dan menyimpannya."""
    logging.info(f"Memulai pembagian data untuk {filename_prefix}...")

    predatory = [entry for entry in data if entry["is_predatory"] == 1]
    non_predatory = [entry for entry in data if entry["is_predatory"] == 0]

    pred_train, pred_test = train_test_split(predatory, train_size=TRAIN_RATIO, random_state=42)
    non_train, non_test = train_test_split(non_predatory, train_size=TRAIN_RATIO, random_state=42)

    train_data = pred_train + non_train
    test_data = pred_test + non_test

    train_path = os.path.join(OUTPUT_DIR, f"{filename_prefix}_train.json")
    test_path = os.path.join(OUTPUT_DIR, f"{filename_prefix}_test.json")

    with open(train_path, "w", encoding="utf-8") as f:
        json.dump(train_data, f, indent=2, ensure_ascii=False)

    with open(test_path, "w", encoding="utf-8") as f:
        json.dump(test_data, f, indent=2, ensure_ascii=False)

    logging.info(f"Data {filename_prefix} berhasil dibagi:")
    logging.info(f"  - Train = {len(train_data)} (Predator: {len(pred_train)}, Non-Predator: {len(non_train)})")
    logging.info(f"  - Test  = {len(test_data)} (Predator: {len(pred_test)}, Non-Predator: {len(non_test)})")

    return {
        "total": {
            "entries": len(data),
            "predatory": total_predatory,
            "non_predatory": total_non_predatory
        },
        "train": {
            "size": len(train_data),
            "predatory": len(pred_train),
            "non_predatory": len(non_train)
        },
        "test": {
            "size": len(test_data),
            "predatory": len(pred_test),
            "non_predatory": len(non_test)
        }
    }

if __name__ == "__main__":
    logging.info("=" * 80)
    logging.info("=== Memulai proses pembagian data ===")
    logging.info("=" * 80)

    summary = {}

    for key, filename in FILES.items():
        logging.info("=" * 80)
        input_path = os.path.join(INPUT_DIR, filename)

        data, total_predatory, total_non_predatory = load_data(input_path)
        summary[key] = split_and_save(data, f"5_{key}")

    log_path = os.path.join(OUTPUT_DIR, "5_split_summary.json")
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    logging.info("=" * 80)
    logging.info("=== Proses pembagian data selesai ===")
    logging.info("=" * 80)
