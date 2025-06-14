import os
import time
import logging
import logging.config
import autosklearn.metrics as metrics
import numpy as np
import joblib
from sklearn.metrics import classification_report, accuracy_score
from pprint import pprint
from autosklearn.classification import AutoSklearnClassifier

# PILIH SALAH SATU TIME_LIMIT
# TIME_LIMIT = 600     # 10 Menit
# TIME_LIMIT = 900     # 15 Menit
# TIME_LIMIT = 1800    # 30 Menit
# TIME_LIMIT = 2700    # 45 Menit
# TIME_LIMIT = 3600    # 60 Menit / 1 Jam
# TIME_LIMIT = 4500    # 75 Menit / 1 Jam 15 Menit
TIME_LIMIT = 5400    # 90 Menit / 1 Jam 30 Menit
# TIME_LIMIT = 6300    # 105 Menit / 1 Jam 45 Menit
# TIME_LIMIT = 7200  # 120 Menit / 2 Jam

METHOD_NAME = "dfs"  # dfs atau bfs
MINUTES = TIME_LIMIT // 60
CLASSIFICATION_DIR = f"8_classification/no_oversampling/{METHOD_NAME}_{MINUTES}min"  # Diubah
os.makedirs(CLASSIFICATION_DIR, exist_ok=True)

LOG_FILE = os.path.join(CLASSIFICATION_DIR, f"8_{METHOD_NAME}_no_oversampling.log")  # Diubah


class NameFilter(logging.Filter):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def filter(self, record):
        return record.name == self.name


logging_configdict = {
    "version": 1,
    "disable_existing_loggers": True,
    "filters": {
        "root_only": {
            "()": NameFilter,
            "name": "root",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": LOG_FILE,
            "level": "INFO",
            "formatter": "simple",
            "filters": ["root_only"],
        },
    },
    "formatters": {
        "simple": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["console", "file"],
    },
    "loggers": {
        "root": {  # Ditambahkan agar konsisten
            "level": "DEBUG",
            "handlers": ["console", "file"],
        },
        "Client-TAE": {
            "level": "CRITICAL",
            "handlers": [],
        },
        "Client-EnsembleBuilder": {
            "level": "CRITICAL",
            "handlers": [],
        },
        "smac": {
            "level": "CRITICAL",
            "handlers": [],
        },
    },
}

logging.config.dictConfig(logging_configdict)


def flush_logs():
    """Memastikan semua log langsung tertulis ke file."""
    for handler in logging.getLogger().handlers:
        handler.flush()


def load_data(vector_path, label_path):
    """Memuat data vektor dan label dari file."""
    if not os.path.exists(vector_path) or not os.path.exists(label_path):
        logging.error(
            f"❌ File tidak ditemukan: {vector_path} atau {label_path}"
        )
        flush_logs()
        return None, None
    X = np.load(vector_path)
    y = np.load(label_path)
    logging.info(f"✅ Data berhasil dimuat. X shape: {X.shape}, y shape: {y.shape}")
    flush_logs()
    return X, y


def train_model(X_train, y_train):
    """Melatih model AutoML."""
    logging.info(f"⏳ Pelatihan dimulai pada: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    flush_logs()
    start_time = time.time()

    automl = AutoSklearnClassifier(
        time_left_for_this_task=TIME_LIMIT,
        n_jobs=2,
        seed=42,
        memory_limit=8192,
        logging_config=logging_configdict,
        metric=metrics.balanced_accuracy,
    )

    logging.info("🔍 Memulai training model...")
    flush_logs()
    automl.fit(X_train, y_train)

    training_time = time.time() - start_time
    logging.info("✅ Training selesai!")
    logging.info(
        f"⏳ TOTAL WAKTU PELATIHAN: {training_time:.2f} detik ({training_time / 60:.2f} menit)"
    )
    logging.info(f"⌛ Pelatihan selesai pada: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    flush_logs()

    return automl


def save_model(model, model_path):
    """Menyimpan model terlatih ke file."""
    joblib.dump(model, model_path)
    logging.info(f"✅ Model disimpan ke {model_path}")
    flush_logs()


def evaluate_model(model, X_test, y_test, method_name):
    """Menguji model dengan data uji dan mencetak hasil evaluasi."""
    logging.info("=" * 80)
    logging.info("📌 Memulai Pengujian Model: %s", method_name)
    logging.info("=" * 80)

    y_pred = model.predict(X_test)

    report = classification_report(
        y_test,
        y_pred,
        target_names=["Non-Predator", "Predator"],
        # labels=[0, 1],
        digits=4,
        zero_division=0,
    )

    logging.info("📊 Hasil Evaluasi Model %s:\n%s", method_name, report)

    accuracy = accuracy_score(y_test, y_pred)
    logging.info(f"🎯 Akurasi Model: {accuracy:.4f}")

    result_file = os.path.join(
        CLASSIFICATION_DIR, f"8_{method_name.lower()}_classification_report.txt" #Diubah
    )
    with open(result_file, "w") as f:
        f.write(report)
        f.write(f"\nAkurasi: {accuracy:.4f}") #Ditambahkan akurasi di file laporan


    logging.info("💾 Laporan hasil disimpan di: %s", result_file)


if __name__ == "__main__":
    """Alur utama untuk melatih dan menyimpan model AutoML."""
    logging.info("=" * 80)
    logging.info(f"🚀 MEMULAI PELATIHAN MODEL: {METHOD_NAME.upper()} | Durasi: {MINUTES} Menit")
    logging.info("=" * 80)
    flush_logs()

    # Path file training
    train_vector_path = (
        f"6_vectorized_journal_data/6_{METHOD_NAME}_train_vectors.npy" #Diubah
    )
    train_label_path = (
        f"6_vectorized_journal_data/6_{METHOD_NAME}_train_labels.npy"  #Diubah
    )
    model_path = os.path.join(
        CLASSIFICATION_DIR, f"8_{METHOD_NAME}_model.pkl" #Diubah
    )

    # Path file pengujian
    test_vector_path = f"6_vectorized_journal_data/6_{METHOD_NAME.lower()}_test_vectors.npy"
    test_label_path = f"6_vectorized_journal_data/6_{METHOD_NAME.lower()}_test_labels.npy"

    X_train, y_train = load_data(train_vector_path, train_label_path)

    if X_train is None or y_train is None:
        logging.error("❌ Data pelatihan tidak tersedia, keluar dari program.")
        flush_logs()
        logging.shutdown()
        exit()

    model = train_model(X_train, y_train)

    if model:
        save_model(model, model_path)

        logging.info("🏆 Leaderboard Model:")
        logging.info(
            "\n%s", model.leaderboard()
        )
        flush_logs()

        logging.info("💡 Ensemble Model:")
        logging.info("\n%s", pprint(model.show_models(), indent=4))
        flush_logs()

        X_test, y_test = load_data(test_vector_path, test_label_path)

        if X_test is not None and y_test is not None:
            evaluate_model(model, X_test, y_test, METHOD_NAME)
        else:
            logging.error("❌ Data pengujian tidak tersedia, tidak dapat mengevaluasi model.")
            flush_logs()
    else:
        logging.error("❌ Model tidak berhasil dilatih, tidak dapat dievaluasi.")
        flush_logs()

    logging.info("=" * 80)
    logging.info("✅ Selesai")
    logging.info("=" * 80)
    flush_logs()

    logging.shutdown()
