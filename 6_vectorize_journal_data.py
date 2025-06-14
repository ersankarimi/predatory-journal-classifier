import json
import os
import time
import numpy as np
import logging
from gensim.models.doc2vec import Doc2Vec, TaggedDocument


INPUT_DIR = "5_split_data"
OUTPUT_DIR = "6_vectorized_journal_data"
os.makedirs(OUTPUT_DIR, exist_ok=True)

LOG_FILE = os.path.join(OUTPUT_DIR, "6_vectorization.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ],
)

VECTOR_SIZE = 100
WINDOW = 5
MIN_COUNT = 1
EPOCHS = 20

FILES = [
    {"name": "bfs_train", "file": "5_bfs_train.json"},
    {"name": "bfs_test", "file": "5_bfs_test.json"},
    {"name": "dfs_train", "file": "5_dfs_train.json"},
    {"name": "dfs_test", "file": "5_dfs_test.json"},
]

time_log = {}

def load_data(filepath):
    """Membaca dataset dari file JSON dan mengembalikan daftar corpus DOM dan label."""
    start_time = time.time()

    logging.info(f"📥 Memuat data dari {filepath}...")
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    dom_corpus = [item["dom_corpus"] for item in data]
    labels = np.array([item["is_predatory"] for item in data])  # Ambil label
    logging.info(f"✅ Total entri: {len(dom_corpus)} dari {filepath}")

    duration = time.time() - start_time
    time_log[filepath] = {"load_data": duration}
    return dom_corpus, labels

def save_labels(labels, output_label_path):
    """Menyimpan label ke file .npy."""
    np.save(output_label_path, labels)
    logging.info(f"✅ Label disimpan di {output_label_path}. Shape: {labels.shape}")

def train_doc2vec(corpus, model_path):
    """Melatih dan menyimpan model Doc2Vec."""
    start_time = time.time()

    tagged_data = [TaggedDocument(words=words, tags=[str(idx)]) for idx, words in enumerate(corpus)]

    logging.info("🛠️ Inisialisasi model Doc2Vec...")
    model = Doc2Vec(vector_size=VECTOR_SIZE, window=WINDOW, min_count=MIN_COUNT, dm=1, epochs=EPOCHS)

    logging.info("📌 Membangun vocabulary...")
    model.build_vocab(tagged_data)

    logging.info("🚀 Memulai proses training...")
    model.train(tagged_data, total_examples=model.corpus_count, epochs=model.epochs)

    logging.info(f"💾 Menyimpan model ke {model_path}...")
    model.save(model_path)

    duration = time.time() - start_time
    time_log[model_path] = {"train_doc2vec": duration}

    return model

def infer_vectors(model, corpus, output_path):
    """Menghasilkan vektor dari teks menggunakan model Doc2Vec."""
    start_time = time.time()

    logging.info(f"📊 Menghasilkan vektor untuk {output_path}...")
    vectors = np.array([model.infer_vector(words) for words in corpus])

    np.save(output_path, vectors)
    logging.info(f"✅ Vektor berhasil disimpan dalam {output_path}. Shape: {vectors.shape}")

    duration = time.time() - start_time
    time_log[output_path] = {"infer_vectors": duration}

if __name__ == "__main__":
    logging.info("=" * 80)
    logging.info("=== Memulai proses vektorisasi dengan Doc2Vec ===")
    logging.info("=" * 80)

    trained_models = {}

    for file_set in FILES:
        name = file_set["name"]
        input_path = os.path.join(INPUT_DIR, file_set["file"])
        output_vector_path = os.path.join(OUTPUT_DIR, f"6_{name}_vectors.npy")
        output_label_path = os.path.join(OUTPUT_DIR, f"6_{name}_labels.npy")

        logging.info("=" * 80)
        logging.info(f"🚀 Memproses file: {file_set['file']} ({name})")
        logging.info("=" * 80)

        corpus, labels = load_data(input_path)

        save_labels(labels, output_label_path)

        if "train" in name:
            model_path = os.path.join(OUTPUT_DIR, f"6_doc2vec_{name}.model")
            model = train_doc2vec(corpus, model_path)
            trained_models[name] = model
        else:
            model_type = name.replace("_test", "_train")
            model = trained_models.get(model_type)

            if model is None:
                logging.error(f"❌ Model {model_type} belum tersedia! Pastikan train diproses lebih dulu.")
                continue

        infer_vectors(model, corpus, output_vector_path)

    time_log_path = os.path.join(OUTPUT_DIR, "6_execution_time.json")
    with open(time_log_path, "w", encoding="utf-8") as f:
        json.dump(time_log, f, indent=4)

    logging.info("=" * 80)
    logging.info("=== Proses vektorisasi selesai ===")
    logging.info(f"📊 Log waktu eksekusi disimpan di {time_log_path}")
    logging.info("=" * 80)
