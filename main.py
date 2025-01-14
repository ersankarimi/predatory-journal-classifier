import pandas as pd
import os
import requests
from bs4 import BeautifulSoup
import json
import logging
from datetime import datetime
from colorama import Fore, Style, init
from requests.exceptions import SSLError
import warnings

# ===== INITIAL SETUP =====
# Inisialisasi colorama untuk output b`erwarna
init(autoreset=True)

# Mode program: 'development' (5 data), 'preview' (20 data), atau 'production' (semua data)
MODE = 'production'

# Buat folder untuk menyimpan data
os.makedirs('temp_data', exist_ok=True)


# ===== LOGGER SETUP =====
class CustomLogFormatter(logging.Formatter):
    """Format logger dengan warna berbeda untuk setiap level"""
    LEVEL_COLORS = {
        "DEBUG": Fore.BLUE,
        "INFO": Fore.GREEN,
        "WARNING": Fore.YELLOW,
        "ERROR": Fore.RED,
        "CRITICAL": Fore.MAGENTA
    }

    def format(self, record):
        color = self.LEVEL_COLORS.get(record.levelname, "")
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        message = super().format(record)
        return f"{color}[{timestamp}] {record.levelname}: {message}{Style.RESET_ALL}"


def setup_logger():
    """Setup sistem logging"""
    logger = logging.getLogger('journal_scraper')
    logger.setLevel(logging.INFO)

    # Setup console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(CustomLogFormatter())

    # Setup file handler
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    file_handler = logging.FileHandler(f'temp_data/scraper_{timestamp}.log')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger


# Inisialisasi logger
logger = setup_logger()


# Konfigurasi warning handler
def log_warning(message, category, filename, lineno, file=None, line=None):
    logger.warning(f"{category.__name__} - {message} in {filename} at line {lineno}")


warnings.showwarning = log_warning


# ===== SCRAPING FUNCTIONS =====
def extract_dom_structure(body):
    """Ekstrak struktur DOM dari HTML body secara rekursif"""

    def recursive_extract(element):
        if not element:
            return []

        children = [
            {
                'tag': child.name,
                'text': child.get_text(strip=True)[:100],
                'children': recursive_extract(child)
            }
            for child in element.find_all(recursive=False)
            if child.name is not None
        ]
        return children

    return recursive_extract(body)


def scrape_url(url, journal_name):
    """Scrape konten webpage dan ekstrak struktur DOM"""
    try:
        logger.info(f"\n{'-' * 40}\nMencoba scraping:\n\tNama Jurnal: {journal_name}\n\tURL: {url}\n{'-' * 40}")

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=13)

        if response.status_code != 200:
            raise SSLError(f"Gagal melakukan koneksi: {url}")

        soup = BeautifulSoup(response.text, 'html.parser')
        body = soup.find('body')

        if body is None:
            raise ValueError(f"Body tidak ditemukan di: {url}")

        dom_structure = extract_dom_structure(body)
        logger.info(f"Berhasil scraping jurnal: {journal_name}\n\n")

        return {
            'url': url,
            'dom_structure': dom_structure
        }

    except (ValueError, SSLError, Exception) as e:
        error_type = type(e).__name__
        logger.error(f"\n{'!' * 40}\n{error_type}:\n\tNama Jurnal: {journal_name}\n\tError: {str(e)}\n{'!' * 40}")
        failed_scrapes.append({
            'journal_name': journal_name,
            'url': url,
            'error_type': error_type,
            'error_message': str(e)
        })
        return None


# ===== DATA LOADING AND PREPROCESSING =====
def load_datasets():
    """Load dan preprocessing dataset jurnal"""
    logger.info(f"\n{'=' * 50}\nMemuat datasets...\n{'=' * 50}")
    try:
        # Load datasets
        doaj_dataset = pd.read_csv('./datasets/journalcsv__doaj_20250105_1420_utf8.csv')
        predatory_dataset = pd.read_csv('./datasets/predatory_Journals.csv')

        logger.info(f"Dataset DOAJ dimuat: {len(doaj_dataset)} entries")
        logger.info(f"Dataset Predatory dimuat: {len(predatory_dataset)} entries")

        return doaj_dataset, predatory_dataset

    except Exception as e:
        logger.critical(f"Error kritis saat memuat dataset: {str(e)}")
        raise


def prepare_datasets(doaj_dataset, predatory_dataset):
    """Persiapkan dan gabungkan dataset berdasarkan mode operasi"""
    # Pilih kolom yang relevan dan buat salinan DataFrame
    doaj_dataset = doaj_dataset[['Journal title', 'Journal URL']].copy()
    doaj_dataset.columns = ['journal_name', 'journal_link']
    doaj_dataset['is_predatory'] = 0

    predatory_dataset = predatory_dataset[['Journals', 'Links']].copy()
    predatory_dataset.columns = ['journal_name', 'journal_link']
    predatory_dataset['is_predatory'] = 1

    # Sesuaikan ukuran dataset berdasarkan mode
    if MODE == 'development':
        doaj_dataset = doaj_dataset.head(5)
        predatory_dataset = predatory_dataset.head(5)
        logger.info("Menjalankan mode development dengan 5 sampel")
    elif MODE == 'preview':
        doaj_dataset = doaj_dataset.head(20)
        predatory_dataset = predatory_dataset.head(20)
        logger.info("Menjalankan mode preview dengan 20 sampel")
    else:
        logger.info("Menjalankan mode production dengan dataset lengkap")

    # Gabung dataset
    merged_dataset = pd.concat([doaj_dataset, predatory_dataset], ignore_index=True)
    logger.info(f"Total jurnal yang akan diproses: {len(merged_dataset)}")

    # Simpan dataset gabungan
    merged_dataset.to_csv('temp_data/merged_journals.csv', index=False)

    return merged_dataset


# ===== MAIN EXECUTION =====
if __name__ == "__main__":
    # Inisialisasi list untuk scraping yang gagal
    failed_scrapes = []

    # Load dan persiapkan dataset
    doaj_dataset, predatory_dataset = load_datasets()
    merged_dataset = prepare_datasets(doaj_dataset, predatory_dataset)

    # Main scraping loop
    logger.info(f"\n{'=' * 50}\nMemulai proses scraping...\n{'=' * 50}")
    results = []
    total_journals = len(merged_dataset)

    for idx, (_, journal) in enumerate(merged_dataset.iterrows(), start=1):
        logger.info(f"Scraping data {idx} dari {total_journals}: {journal['journal_name']}")
        result = scrape_url(journal['journal_link'], journal['journal_name'])
        if result:
            results.append(result)

    # Simpan hasil
    logger.info(f"\n{'=' * 50}\nMenyimpan hasil scraping...\n{'=' * 50}")
    with open('temp_data/scraped_journals.json', 'w') as f:
        json.dump(results, f, indent=2)

    # Simpan data yang gagal
    if failed_scrapes:
        failed_scrapes_df = pd.DataFrame(failed_scrapes)
        failed_scrapes_df = failed_scrapes_df[['journal_name', 'url', 'error_type', 'error_message']]
        failed_scrapes_df.to_csv('temp_data/scrape_failures.csv', index=False)
        logger.warning(f"Menyimpan {len(failed_scrapes)} scraping yang gagal ke scrape_failures.csv")

    # Tampilkan statistik akhir
    total_successful_scrapes = len(results)
    total_failed_scrapes = len(failed_scrapes)

    logger.info(f"\n{'=' * 50}\nStatistik Akhir:\n{'=' * 50}")
    logger.info(f"Total Data Awal: {len(merged_dataset)}")
    logger.info(f"Berhasil Scraping: {total_successful_scrapes}")
    logger.info(f"Gagal Scraping: {total_failed_scrapes}")
    logger.info(f"Persentase Keberhasilan: {(total_successful_scrapes / len(merged_dataset) * 100):.2f}%")

    logger.info(f"\n{'=' * 50}\nPersiapan data dan scraping selesai.\n{'=' * 50}")

# Bagian Doc2Vec (dikomentari)
"""
# Bagian ini untuk proses Doc2Vec yang akan diimplementasikan nanti

print(f"\n{'='*50}\nMemproses struktur DOM...\n{'='*50}")
with open('temp_data/scraped_journals.json', 'r') as f:
    scraped_data = json.load(f)

# ... Kode Doc2Vec akan ditambahkan di sini ...
"""
