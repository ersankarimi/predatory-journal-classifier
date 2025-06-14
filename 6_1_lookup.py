import os
import json
import numpy as np
import logging
from gensim.models.doc2vec import Doc2Vec

# Direktori hasil vektorisasi
VECTOR_DIR = "6_vectorized_journal_data"
INPUT_DIR = "5_split_data"

LOG_FILE = os.path.join(VECTOR_DIR, "6_1_lookup.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ],
)

def inspect_doc2vec(model_path):
    """Membaca dan menampilkan informasi dari model Doc2Vec."""
    logging.info(f"📥 Memuat model: {model_path}")

    model = Doc2Vec.load(model_path)

    logging.info(f"📌 Dimensi vektor: {model.vector_size}")
    logging.info(f"📌 Jumlah kata dalam vocabulary: {len(model.wv.index_to_key)}")

    # Cek 10 kata paling sering muncul
    common_words = model.wv.index_to_key[:10]
    logging.info(f"🔍 10 Kata Paling Sering Muncul: {common_words}")

    # Cek vektor salah satu kata dalam vocabulary
    if common_words:
        sample_word = common_words[0]
        logging.info(f"🧩 Vektor kata '{sample_word}': {model.wv[sample_word]}")

def inspect_vectors(npy_path):
    """Membaca dan menampilkan informasi dari file .npy."""
    logging.info(f"📥 Memuat file vektor: {npy_path}")

    vectors = np.load(npy_path)

    logging.info(f"📌 Bentuk array vektor: {vectors.shape}")
    logging.info(f"🔍 5 Vektor pertama:\n{vectors[:5]}")

def check_data_distribution(json_path):
    """Memeriksa distribusi label di file JSON."""
    logging.info(f"📥 Memuat file label: {json_path}")

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    y_labels = np.array([item["is_predatory"] for item in data])
    class_distribution = np.bincount(y_labels)

    logging.info(f"📊 Distribusi kelas: {class_distribution}")

if __name__ == "__main__":
    logging.info("=" * 80)
    logging.info("=== Memulai pengecekan hasil vektorisasi ===")
    logging.info("=" * 80)

    FILES = ["bfs", "dfs"]

    for name in FILES:
        logging.info(f"\n🔎 **Memeriksa hasil untuk metode: {name.upper()}**")

        # 1️⃣ Periksa model Doc2Vec
        model_path = os.path.join(VECTOR_DIR, f"6_doc2vec_{name}_train.model")
        if os.path.exists(model_path):
            inspect_doc2vec(model_path)
        else:
            logging.warning(f"⚠️ Model {model_path} tidak ditemukan!")

        # 2️⃣ Periksa vektor train
        train_vector_path = os.path.join(VECTOR_DIR, f"6_{name}_train_vectors.npy")
        if os.path.exists(train_vector_path):
            inspect_vectors(train_vector_path)
        else:
            logging.warning(f"⚠️ Vektor train {train_vector_path} tidak ditemukan!")

        # 3️⃣ Periksa vektor test
        test_vector_path = os.path.join(VECTOR_DIR, f"6_{name}_test_vectors.npy")
        if os.path.exists(test_vector_path):
            inspect_vectors(test_vector_path)
        else:
            logging.warning(f"⚠️ Vektor test {test_vector_path} tidak ditemukan!")

        # 4️⃣ Periksa distribusi kelas untuk train
        train_label_path = os.path.join(INPUT_DIR, f"5_{name}_train.json")
        if os.path.exists(train_label_path):
            check_data_distribution(train_label_path)
        else:
            logging.warning(f"⚠️ Label train {train_label_path} tidak ditemukan!")

        # 5️⃣ Periksa distribusi kelas untuk test
        test_label_path = os.path.join(INPUT_DIR, f"5_{name}_test.json")
        if os.path.exists(test_label_path):
            check_data_distribution(test_label_path)
        else:
            logging.warning(f"⚠️ Label test {test_label_path} tidak ditemukan!")

    logging.info("=" * 80)
    logging.info("=== Pengecekan selesai ===")
    logging.info("=" * 80)
