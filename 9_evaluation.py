import os
import numpy as np
import joblib
import logging
from sklearn.metrics import classification_report

# Direktori penyimpanan hasil evaluasi
EVALUATION_DIR = "9_evaluation"
os.makedirs(EVALUATION_DIR, exist_ok=True)

# Konfigurasi logging
LOG_FILE = os.path.join(EVALUATION_DIR, "9_evaluation.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ],
)


def load_data(vector_path, label_path):
    """Memuat data vektor dan label dari file."""
    X_test = np.load(vector_path)
    y_test = np.load(label_path)

    # saya mau liat isi array dari X_test dan label dari y_test
    print(X_test.shape, y_test.shape)

    # print(X_test[:5, :10])  # 5 baris pertama, 10 kolom pertama

    print(y_test)  # 5 label pertama






    print(X_test.shape, y_test.shape)
    return X_test, y_test


def evaluate_model(model_path, X_test, y_test, method_name):
    """Menguji model dengan data uji dan mencetak hasil evaluasi."""
    logging.info("=" * 80)
    logging.info("📌 Memulai Pengujian Model: %s", method_name)
    logging.info("=" * 80)

    # Load model
    model = joblib.load(model_path)
    logging.info("✅ Model dimuat dari: %s", model_path)

    # Prediksi data uji
    y_pred = model.predict(X_test)

    # Evaluasi performa
    report = classification_report(y_test, y_pred, target_names=["Non-Predator", "Predator"], digits=4)

    logging.info("📊 Hasil Evaluasi Model %s:\n%s", method_name, report)

    # Simpan hasil evaluasi ke file
    result_file = os.path.join(EVALUATION_DIR, f"9_{method_name.lower()}_classification_report.txt")
    with open(result_file, "w") as f:
        f.write(report)

    logging.info("💾 Laporan hasil disimpan di: %s", result_file)


# File dataset uji
datasets = {
    # "BFS": {
    #     "vector": "6_vectorized_journal_data/6_bfs_test_vectors.npy",
    #     "label": "6_vectorized_journal_data/6_bfs_test_labels.npy",
    #     "model": "8_classification/8_bfs_model.pkl"
    # },
    "DFS": {
        "vector": "6_vectorized_journal_data/6_dfs_test_vectors.npy",
        "label": "6_vectorized_journal_data/6_dfs_test_labels.npy",
        "model": "8_classification/8_dfs_model.pkl"
    }
}

# Proses pengujian untuk BFS dan DFS
for method, paths in datasets.items():
  X_test, y_test = load_data(paths["vector"], paths["label"])
  print(X_test.shape, y_test.shape)
  evaluate_model(paths["model"], X_test, y_test, method)

logging.info("=" * 80)
logging.info("🎯 Semua proses evaluasi model selesai.")
logging.info("=" * 80)
