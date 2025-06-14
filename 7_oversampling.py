import os
import json
import numpy as np
import logging
from imblearn.combine import SMOTEENN

# Direktori input dan output
SPLIT_DIR = "5_split_data"
VECTOR_DIR = "6_vectorized_journal_data"
OVERSAMPLING_DIR = "7_oversampling"
os.makedirs(OVERSAMPLING_DIR, exist_ok=True)

LOG_FILE = os.path.join(OVERSAMPLING_DIR, "7_oversampling.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ],
)

# File yang akan diproses
FILES = ["bfs", "dfs"]

def load_labels(filepath):
    """Membaca label dari file JSON dan mengembalikannya sebagai array NumPy."""
    if not os.path.exists(filepath):
        logging.error(f"❌ File tidak ditemukan: {filepath}")
        return None

    logging.info(f"📥 Memuat label dari {filepath}...")
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    y_train = np.array([item["is_predatory"] for item in data])
    logging.info(f"✅ Total label: {len(y_train)}")
    return y_train

def load_vectors(filepath):
    """Memuat vektor dari file NPY."""
    if not os.path.exists(filepath):
        logging.error(f"❌ File tidak ditemukan: {filepath}")
        return None

    logging.info(f"📥 Memuat vektor dari {filepath}...")
    X_train = np.load(filepath)
    logging.info(f"✅ Shape vektor: {X_train.shape}")
    return X_train

def check_distribution(y_train, phase="Sebelum Oversampling"):
    """Melakukan pengecekan distribusi data dan mencetak hasilnya."""
    predator_count = np.sum(y_train == 1)
    non_predator_count = np.sum(y_train == 0)

    logging.info(f"📊 **Distribusi Data - {phase}**")
    logging.info(f"   - Jurnal Predator      : {predator_count}")
    logging.info(f"   - Jurnal Non-Predator  : {non_predator_count}")

def perform_oversampling(X_train, y_train):
    """Melakukan oversampling menggunakan SMOTEENN dan mengembalikan data yang telah di-resample."""
    logging.info("⚙️ **Proses Oversampling Menggunakan SMOTEENN...**")
    smoteenn = SMOTEENN(random_state=42)
    X_resampled, y_resampled = smoteenn.fit_resample(X_train, y_train)

    logging.info("✅ Oversampling selesai.")
    return X_resampled, y_resampled

def save_oversampled_data(name, X_resampled, y_resampled):
    """Menyimpan data hasil oversampling ke dalam file NPY."""
    vector_path = os.path.join(OVERSAMPLING_DIR, f"7_{name}_train_vectors_oversampled.npy")
    label_path = os.path.join(OVERSAMPLING_DIR, f"7_{name}_train_labels_oversampled.npy")

    np.save(vector_path, X_resampled)
    np.save(label_path, y_resampled)

    logging.info(f"💾 **Hasil Oversampling Disimpan:**")
    logging.info(f"   → Vektor   : {vector_path}")
    logging.info(f"   → Label    : {label_path}")

if __name__ == "__main__":
    logging.info("=" * 80)
    logging.info("=== Memulai Proses Oversampling Data ===")
    logging.info("=" * 80)

    for name in FILES:
        logging.info("=" * 80)
        logging.info(f"🚀 Memproses metode: {name.upper()}")
        logging.info("=" * 80)

        # Path file
        label_path = os.path.join(SPLIT_DIR, f"5_{name}_train.json")
        vector_path = os.path.join(VECTOR_DIR, f"6_{name}_train_vectors.npy")

        # Memuat data
        y_train = load_labels(label_path)
        X_train = load_vectors(vector_path)

        if y_train is None or X_train is None:
            logging.error(f"❌ Melewati {name.upper()} karena file tidak ditemukan.")
            continue

        # Cek distribusi sebelum oversampling
        check_distribution(y_train, phase="Sebelum Oversampling")

        # Oversampling
        X_resampled, y_resampled = perform_oversampling(X_train, y_train)

        # Cek distribusi setelah oversampling
        check_distribution(y_resampled, phase="Setelah Oversampling")

        # Simpan hasil
        save_oversampled_data(name, X_resampled, y_resampled)

    logging.info("=" * 80)
    logging.info("🎯 **Proses Oversampling Selesai**")
    logging.info("=" * 80)
