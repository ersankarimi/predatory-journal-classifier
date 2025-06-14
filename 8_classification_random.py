import os
import time
import logging
import logging.config
import numpy as np
import joblib
from autosklearn.classification import AutoSklearnClassifier
from sklearn.metrics import classification_report, accuracy_score
from pprint import pprint

# -------------------- KONFIGURASI UTAMA --------------------
METHOD_NAME = "bfs"  # contoh: dfs, bfs, opti, dst
# TIME_LIMIT = 1800  # 30 Menit
# TIME_LIMIT = 3600  # 60 Menit
# TIME_LIMIT = 5400  # 90 Menit
TIME_LIMIT = 7200  # 120 Menit

RUN_NAME = f"{METHOD_NAME}_random_{TIME_LIMIT // 60}min"

BASE_DIR = "8_classification_random"
CLASSIFICATION_DIR = os.path.join(BASE_DIR, RUN_NAME)
TEMP_DIR = os.path.join(CLASSIFICATION_DIR, "tmp")

os.makedirs(CLASSIFICATION_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)

LOG_FILE = os.path.join(CLASSIFICATION_DIR, f"{RUN_NAME}.log")
MODEL_FILE = os.path.join(CLASSIFICATION_DIR, f"{RUN_NAME}_model.pkl")
REPORT_FILE = os.path.join(CLASSIFICATION_DIR, f"{RUN_NAME}_classification_report.txt")

# Path file training dan testing
TRAIN_VECTOR_PATH = f"7_oversampling_random/7_{METHOD_NAME}_train_vectors_oversampled.npy"
TRAIN_LABEL_PATH = f"7_oversampling_random/7_{METHOD_NAME}_train_labels_oversampled.npy"
TEST_VECTOR_PATH = f"6_vectorized_journal_data/6_{METHOD_NAME}_test_vectors.npy"
TEST_LABEL_PATH = f"6_vectorized_journal_data/6_{METHOD_NAME}_test_labels.npy"


# -------------------- SETUP LOGGING --------------------
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
        "root": {
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


# -------------------- UTILITY FUNCTION --------------------
def flush_logs():
    for handler in logging.getLogger().handlers:
        handler.flush()


def load_data(vector_path, label_path):
    if not os.path.exists(vector_path) or not os.path.exists(label_path):
        logging.error(f"❌ File tidak ditemukan: {vector_path} atau {label_path}")
        flush_logs()
        return None, None
    X = np.load(vector_path)
    y = np.load(label_path)
    logging.info(f"✅ Data berhasil dimuat. X shape: {X.shape}, y shape: {y.shape}")
    flush_logs()
    return X, y


def train_model(X_train, y_train):
    logging.info(f"⏳ Pelatihan dimulai pada: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    flush_logs()
    start_time = time.time()

    automl = AutoSklearnClassifier(
        time_left_for_this_task=TIME_LIMIT,
        n_jobs=2,
        seed=42,
        memory_limit=8192,
        logging_config=logging_configdict,
    )

    logging.info("🔍 Memulai training model...")
    flush_logs()
    automl.fit(X_train, y_train)

    training_time = time.time() - start_time
    logging.info("✅ Training selesai!")
    logging.info(f"⏳ TOTAL WAKTU PELATIHAN: {training_time:.2f} detik ({training_time / 60:.2f} menit)")
    logging.info(f"⌛ Pelatihan selesai pada: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    flush_logs()

    return automl


def save_model(model, model_path):
    joblib.dump(model, model_path)
    logging.info(f"✅ Model disimpan ke {model_path}")
    flush_logs()


def evaluate_model(model, X_test, y_test, method_name):
    logging.info("=" * 80)
    logging.info(f"📌 Memulai Pengujian Model: {method_name}")
    logging.info("=" * 80)

    y_pred = model.predict(X_test)

    report = classification_report(
        y_test,
        y_pred,
        target_names=["Non-Predator", "Predator"],
        digits=4,
        zero_division=0,
    )

    logging.info(f"📊 Hasil Evaluasi Model {method_name}:\n{report}")

    accuracy = accuracy_score(y_test, y_pred)
    logging.info(f"🎯 Akurasi Model: {accuracy:.4f}")

    with open(REPORT_FILE, "w") as f:
        f.write(report)
        f.write(f"\nAkurasi: {accuracy:.4f}")

    logging.info(f"💾 Laporan hasil disimpan di: {REPORT_FILE}")


# -------------------- MAIN SCRIPT --------------------
if __name__ == "__main__":
    logging.info("=" * 80)
    logging.info(f"🚀 MEMULAI PELATIHAN MODEL: {RUN_NAME.upper()}")
    logging.info("=" * 80)
    flush_logs()

    X_train, y_train = load_data(TRAIN_VECTOR_PATH, TRAIN_LABEL_PATH)

    if X_train is None or y_train is None:
        logging.error("❌ Data pelatihan tidak tersedia, keluar dari program.")
        flush_logs()
        logging.shutdown()
        exit()

    model = train_model(X_train, y_train)

    if model:
        save_model(model, MODEL_FILE)

        logging.info("🏆 Leaderboard Model:")
        logging.info("\n%s", model.leaderboard())
        flush_logs()

        logging.info("💡 Ensemble Model:")
        logging.info("\n%s", pprint(model.show_models(), indent=4))
        flush_logs()

        X_test, y_test = load_data(TEST_VECTOR_PATH, TEST_LABEL_PATH)

        if X_test is not None and y_test is not None:
            evaluate_model(model, X_test, y_test, RUN_NAME)
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
