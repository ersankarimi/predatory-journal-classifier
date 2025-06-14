import os
import time
import logging
import logging.config
import numpy as np
import joblib
from autosklearn.classification import AutoSklearnClassifier
from sklearn.metrics import classification_report, accuracy_score
from pprint import pprint

# PILIH SALAH SATU TIME_LIMIT
TIME_LIMIT = 600     # 10 Menit
# TIME_LIMIT = 900     # 15 Menit
# TIME_LIMIT = 1800    # 30 Menit
# TIME_LIMIT = 2700    # 45 Menit
# TIME_LIMIT = 3600    # 60 Menit / 1 Jam
# TIME_LIMIT = 4500    # 75 Menit / 1 Jam 15 Menit
# TIME_LIMIT = 5400    # 90 Menit / 1 Jam 30 Menit
# TIME_LIMIT = 6300    # 105 Menit / 1 Jam 45 Menit
# TIME_LIMIT = 7200  # 120 Menit / 2 Jam

METHOD_NAME = "dfs"  # atau "dfs"
MINUTES = TIME_LIMIT // 60
CLASSIFICATION_DIR = f"8_classification/{METHOD_NAME}_{MINUTES}min"
os.makedirs(CLASSIFICATION_DIR, exist_ok=True)

LOG_FILE = os.path.join(CLASSIFICATION_DIR, f"8_{METHOD_NAME}.log")


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
        "Client-TAE": {"level": "CRITICAL", "handlers": []},
        "Client-EnsembleBuilder": {"level": "CRITICAL", "handlers": []},
        "smac": {"level": "CRITICAL", "handlers": []},
    },
}

logging.config.dictConfig(logging_configdict)


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
    logging.info(f"✅ Data dimuat. X shape: {X.shape}, y shape: {y.shape}")
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
        memory_limit=4096,
        logging_config=logging_configdict,
    )

    logging.info("🔍 Training model...")
    flush_logs()
    automl.fit(X_train, y_train)

    training_time = time.time() - start_time
    logging.info("✅ Training selesai!")
    logging.info(f"⏳ TOTAL WAKTU: {training_time:.2f} detik ({training_time / 60:.2f} menit)")
    flush_logs()
    return automl


def save_model(model, model_path):
    joblib.dump(model, model_path)
    logging.info(f"✅ Model disimpan ke {model_path}")
    flush_logs()


def evaluate_model(model, X_test, y_test, method_name):
    logging.info("=" * 80)
    logging.info("📌 Evaluasi Model: %s", method_name)
    logging.info("=" * 80)

    y_pred = model.predict(X_test)
    report = classification_report(
        y_test, y_pred, target_names=["Non-Predator", "Predator"], digits=4, zero_division=0
    )

    logging.info("📊 Laporan Evaluasi:\n%s", report)
    accuracy = accuracy_score(y_test, y_pred)
    logging.info(f"🎯 Akurasi: {accuracy:.4f}")

    result_file = os.path.join(CLASSIFICATION_DIR, f"8_{method_name.lower()}_classification_report.txt")
    with open(result_file, "w") as f:
        f.write(report)
        f.write(f"\nAkurasi: {accuracy:.4f}")

    logging.info("💾 Laporan disimpan di: %s", result_file)


if __name__ == "__main__":
    logging.info("=" * 80)
    logging.info(f"🚀 MULAI TRAINING MODEL: {METHOD_NAME.upper()} | Durasi: {MINUTES} Menit")
    logging.info("=" * 80)
    flush_logs()

    train_vector_path = f"7_oversampling/7_{METHOD_NAME}_train_vectors_oversampled.npy"
    train_label_path = f"7_oversampling/7_{METHOD_NAME}_train_labels_oversampled.npy"
    model_path = os.path.join(CLASSIFICATION_DIR, f"8_{METHOD_NAME}_model.pkl")

    test_vector_path = f"6_vectorized_journal_data/6_{METHOD_NAME.lower()}_test_vectors.npy"
    test_label_path = f"6_vectorized_journal_data/6_{METHOD_NAME.lower()}_test_labels.npy"

    X_train, y_train = load_data(train_vector_path, train_label_path)
    if X_train is None or y_train is None:
        logging.error("❌ Data pelatihan tidak tersedia.")
        flush_logs()
        logging.shutdown()
        exit()

    model = train_model(X_train, y_train)

    if model:
        save_model(model, model_path)

        logging.info("🏆 Leaderboard:")
        logging.info("\n%s", model.leaderboard())
        flush_logs()

        logging.info("💡 Model Ensemble:")
        logging.info("\n%s", pprint(model.show_models(), indent=4))
        flush_logs()

        X_test, y_test = load_data(test_vector_path, test_label_path)
        if X_test is not None and y_test is not None:
            evaluate_model(model, X_test, y_test, METHOD_NAME)
        else:
            logging.error("❌ Data pengujian tidak tersedia.")
            flush_logs()
    else:
        logging.error("❌ Model gagal dilatih.")
        flush_logs()

    logging.info("=" * 80)
    logging.info("✅ Selesai")
    logging.info("=" * 80)
    flush_logs()
    logging.shutdown()
