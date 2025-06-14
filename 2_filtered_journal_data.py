import os
import pandas as pd
import logging

INPUT_FILE = "1_combined_journal_data/1_combined_journal_data.csv"
OUTPUT_DIR = "2_filtered_journal_data"
FILTERED_FILE = os.path.join(OUTPUT_DIR, "2_filtered_journal_data.csv")
REMOVED_FILE = os.path.join(OUTPUT_DIR, "2_filtered_journal_data_removed.csv")
DUPLICATE_LOG_FILE = os.path.join(OUTPUT_DIR, "2_filtered_journal_duplicates.log")
LOG_FILE = os.path.join(OUTPUT_DIR, "2_filtered_journal_data.log")

os.makedirs(OUTPUT_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S"))
logging.getLogger().addHandler(console_handler)

duplicate_logger = logging.getLogger("duplicate_logger")
duplicate_logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(DUPLICATE_LOG_FILE, mode="w", encoding="utf-8")
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s", "%Y-%m-%d %H:%M:%S"))
duplicate_logger.addHandler(file_handler)

def normalize_url(url):
    return str(url).strip().lower().rstrip("/")

def write_log(message, separator=False):
    if separator:
        logging.info("\n" + "=" * 50)
    logging.info(message)
    if separator:
        logging.info("=" * 50 + "\n")

def filter_data():
    write_log("Memulai proses filtering data...", separator=True)

    write_log(f"Membaca dataset: {INPUT_FILE}...")
    df = pd.read_csv(INPUT_FILE, encoding="utf-8", dtype=str)

    df["is_predatory"] = df["is_predatory"].astype(int)

    total_awal = len(df)
    total_predator_awal = len(df[df["is_predatory"] == 1])
    total_non_predator_awal = len(df[df["is_predatory"] == 0])

    write_log(f"Total data awal: {total_awal}")
    write_log(f"   - Jurnal predator: {total_predator_awal}")
    write_log(f"   - Jurnal non-predator: {total_non_predator_awal}")

    write_log("Melakukan normalisasi URL...")
    df["journal_url"] = df["journal_url"].apply(normalize_url)

    # Pisahkan data yang tidak memiliki URL
    df_no_url = df[df["journal_url"].isna() | (df["journal_url"].str.strip() == "")]
    df = df.dropna(subset=["journal_url"])
    df = df[df["journal_url"].str.strip() != ""]

    total_setelah_hapus_kosong = len(df)
    total_hapus_kosong = total_awal - total_setelah_hapus_kosong
    write_log(f"Total data tanpa URL yang dihapus: {total_hapus_kosong}")

    write_log("Mendeteksi dan membuang semua duplikasi berdasarkan journal_url...")

    duplikat_mask = df.duplicated(subset=["journal_url"], keep=False)
    df_duplikat = df[duplikat_mask]

    if not df_duplikat.empty:
        duplicate_logger.info("\n" + "=" * 50)
        duplicate_logger.info("Detail Jurnal Duplikat berdasarkan journal_url:")
        duplicate_logger.info("=" * 50 + "\n")

        for url, group in df_duplikat.groupby("journal_url"):
            duplicate_logger.info(f"URL: {url}")
            for _, row in group.iterrows():
                duplicate_logger.info(f"   - Judul: {row['journal_title']} | is_predatory: {row['is_predatory']}")
            duplicate_logger.info("-" * 50)

    df = df[~duplikat_mask]

    total_setelah_hapus_duplikat = len(df)
    total_hapus_duplikat = total_setelah_hapus_kosong - total_setelah_hapus_duplikat
    write_log(f"Total data duplikat yang dihapus (semua dibuang): {total_hapus_duplikat}")

    total_akhir = len(df)
    total_predator_akhir = len(df[df["is_predatory"] == 1])
    total_non_predator_akhir = len(df[df["is_predatory"] == 0])

    write_log(f"Total data setelah filtering: {total_akhir}")
    write_log(f"   - Jurnal predator: {total_predator_akhir}")
    write_log(f"   - Jurnal non-predator: {total_non_predator_akhir}")

    df_removed = pd.concat([df_no_url, df_duplikat], ignore_index=True)

    df.to_csv(FILTERED_FILE, index=False, encoding="utf-8")
    write_log(f"File data yang sudah difilter disimpan di: {FILTERED_FILE}")

    df_removed.to_csv(REMOVED_FILE, index=False, encoding="utf-8")
    write_log(f"File data yang terhapus disimpan di: {REMOVED_FILE}")

    write_log("Proses filtering data selesai.", separator=True)

if __name__ == "__main__":
    filter_data()
