import os
import csv
import pandas as pd
import logging
from datetime import datetime
    
# Path file input dan output
DOAJ_FILE = "datasets/journalcsv__doaj_20250105_1420_utf8.csv"
PREDATOR_FILE = "datasets/predatory_Journals.csv"
OUTPUT_DIR = "1_combined_journal_data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "1_combined_journal_data.csv")
LOG_FILE = os.path.join(OUTPUT_DIR, "1_combined_journal_data.log")

# Pastikan output directory ada
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Konfigurasi logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S"))
logging.getLogger().addHandler(console_handler)

# Fungsi untuk mencatat log dengan garis pemisah untuk kejelasan
def write_log(message, separator=False):
    if separator:
        logging.info("\n" + "=" * 50)
    logging.info(message)
    if separator:
        logging.info("=" * 50 + "\n")

# Fungsi untuk mendeteksi delimiter CSV secara otomatis
def detect_delimiter(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        sample = f.read(2048)
        return csv.Sniffer().sniff(sample).delimiter

# Fungsi untuk membaca dataset dengan penanganan karakter non-latin
def load_dataset(file_path, columns, rename_map, is_predatory):
    write_log(f"Mendeteksi delimiter untuk: {file_path}...")
    delimiter = detect_delimiter(file_path)
    write_log(f"Delimiter terdeteksi: '{delimiter}'")

    write_log(f"Membaca dataset: {file_path}...")
    df = pd.read_csv(file_path, sep=delimiter, encoding="utf-8", dtype=str)

    # Hanya mengambil kolom yang tersedia untuk menghindari error
    available_columns = [col for col in columns if col in df.columns]
    df = df[available_columns].rename(columns=rename_map)

    # Tambahkan kolom is_predatory (1 = jurnal predator, 0 = bukan)
    df["is_predatory"] = 1 if is_predatory else 0
    write_log(f"Dataset {file_path} berhasil dibaca dengan {len(df)} baris.")
    return df

# Fungsi utama untuk menggabungkan dataset
def combine_datasets():
    write_log("Memulai proses penggabungan dataset...", separator=True)

    # Load dataset DOAJ
    df_doaj = load_dataset(
        DOAJ_FILE,
        ["Journal title", "Journal URL"],
        {"Journal title": "journal_title", "Journal URL": "journal_url"},
        is_predatory=False
    )
    write_log(f"Total data dari DOAJ: {len(df_doaj)}")

    # Load dataset Predator
    df_predator = load_dataset(
        PREDATOR_FILE,
        ["Journals", "Links"],
        {"Journals": "journal_title", "Links": "journal_url"},
        is_predatory=True
    )
    write_log(f"Total data dari jurnal predator: {len(df_predator)}")

    # Menggabungkan dataset
    write_log("Menggabungkan kedua dataset...")
    df_combined = pd.concat([df_doaj, df_predator], ignore_index=True)
    write_log(f"Total dataset setelah digabung: {len(df_combined)} baris.")

    # Menyimpan hasil ke file CSV
    df_combined.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")
    write_log(f"File gabungan berhasil disimpan di: {OUTPUT_FILE}")

    write_log("Proses penggabungan dataset selesai.", separator=True)

# Jalankan script hanya jika ini file utama
if __name__ == "__main__":
    combine_datasets()
