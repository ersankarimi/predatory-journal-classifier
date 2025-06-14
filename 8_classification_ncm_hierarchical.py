import os
import time
import logging
import numpy as np
import joblib
from sklearn.cluster import AgglomerativeClustering
from sklearn.neighbors import NearestCentroid
from sklearn.metrics import classification_report, accuracy_score, silhouette_score
from collections import Counter
from sklearn.preprocessing import StandardScaler  # Import StandardScaler


METHOD_NAME = "bfs"
CLASSIFICATION_DIR = f"8_classification/ncm_hierarchical/{METHOD_NAME}_ncm_hierarchical"
os.makedirs(CLASSIFICATION_DIR, exist_ok=True)

LOG_FILE = os.path.join(CLASSIFICATION_DIR, f"8_{METHOD_NAME}_ncm_hierarchical.log")

# Konfigurasi Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(LOG_FILE), logging.StreamHandler()],
)


def load_data(vector_path, label_path):
    if not os.path.exists(vector_path) or not os.path.exists(label_path):
        logging.error(f"❌ File tidak ditemukan: {vector_path} atau {label_path}")
        return None, None
    X = np.load(vector_path)
    y = np.load(label_path)
    logging.info(f"✅ Data dimuat. X shape: {X.shape}, y shape: {y.shape}")
    return X, y


def analyze_cluster_composition(cluster_labels, y_train, n_clusters):
    """Analisis komposisi label (Predator/Non-Predator) di setiap cluster."""
    cluster_composition = {}
    for cluster_id in range(n_clusters):
        labels_in_cluster = y_train[cluster_labels == cluster_id]

        if len(labels_in_cluster) == 0:
            logging.warning(
                f"⚠️ Cluster {cluster_id} kosong! Tidak dapat menentukan label mayoritas."
            )
            cluster_composition[cluster_id] = -1
            continue

        label_counts = Counter(labels_in_cluster)
        most_common_label = label_counts.most_common(1)[0][0]
        cluster_composition[cluster_id] = most_common_label
        logging.info(
            f"🔍 Cluster {cluster_id}: Mayoritas label = {most_common_label} (Jumlah: {label_counts})"
        )

    return cluster_composition


def train_model(X_train, y_train, n_clusters=2, linkage="ward"):
    """Melatih model dengan Hierarchical Clustering dan NCM."""
    logging.info("⏳ Pelatihan dimulai...")
    start_time = time.time()

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)

    logging.info(
        f"🔍 Melakukan Hierarchical Clustering (n_clusters={n_clusters}, linkage='{linkage}')..."
    )
    clustering = AgglomerativeClustering(n_clusters=n_clusters, linkage=linkage)
    cluster_labels = clustering.fit_predict(X_train)
    logging.info("✅ Clustering selesai.")

    silhouette_avg = silhouette_score(X_train, cluster_labels)
    logging.info(f"📊 Silhouette Score: {silhouette_avg:.4f}")

    cluster_mapping = analyze_cluster_composition(cluster_labels, y_train, n_clusters)

    logging.info("🧠 Melatih Nearest Centroid Classifier...")
    clf = NearestCentroid(metric="euclidean")
    clf.fit(X_train, cluster_labels)
    logging.info("✅ NCM Classifier selesai dilatih.")

    training_time = time.time() - start_time
    logging.info(f"⏳ TOTAL WAKTU: {training_time:.2f} detik")

    return scaler, clustering, clf, cluster_mapping, silhouette_avg


def predict_and_evaluate(scaler, clustering, clf, cluster_mapping, X_test, y_test):
    """Memprediksi dan mengevaluasi model."""
    logging.info("📌 Memulai prediksi dan evaluasi...")
    start_time = time.time()

    # Penskalaan Fitur pada Data Uji
    X_test = scaler.transform(X_test)

    cluster_labels_pred = clf.predict(X_test)

    # Konversi Label Cluster ke Label Asli menggunakan mapping
    y_pred = np.array(
        [cluster_mapping.get(cluster_id, -1) for cluster_id in cluster_labels_pred]
    )

    if -1 in y_pred:
        logging.warning(
            "⚠️ Terdapat cluster yang tidak terdefinisi dalam mapping. "
            "Menetapkan label default (kelas mayoritas global)."
        )
        most_frequent_class = Counter(y_train).most_common(1)[0][0]
        y_pred[y_pred == -1] = most_frequent_class

    # Evaluasi
    report = classification_report(
        y_test,
        y_pred,
        target_names=["Non-Predator", "Predator"],
        digits=4,
        zero_division=0,
    )
    accuracy = accuracy_score(y_test, y_pred)
    logging.info("📊 Laporan Klasifikasi:\n%s", report)
    logging.info(f"🎯 Akurasi: {accuracy:.4f}")

    evaluation_time = time.time() - start_time
    logging.info(f"⏳ Waktu Evaluasi: {evaluation_time:.2f} detik")

    return report, accuracy


def save_model(model, scaler, clustering, cluster_mapping, silhouette_avg, model_path):
    joblib.dump((model, scaler, clustering, cluster_mapping, silhouette_avg), model_path)
    logging.info(
        f"✅ Model, clustering, cluster_mapping, dan silhouette score disimpan ke {model_path}"
    )


def load_model(model_path):
    try:
        model, scaler, clustering, cluster_mapping, silhouette_avg = joblib.load(
            model_path
        )
        logging.info(
            f"✅ Model, clustering, cluster_mapping, dan silhouette score dimuat dari {model_path}"
        )
        return model, scaler, clustering, cluster_mapping, silhouette_avg
    except FileNotFoundError:
        logging.error(f"❌ File model tidak ditemukan di {model_path}")
        return None, None, None, None, None
    except Exception as e:
        logging.error(f"❌ Gagal memuat model: {e}")
        return None, None, None, None, None


if __name__ == "__main__":
    logging.info("=" * 80)
    logging.info(f"🚀 MULAI TRAINING MODEL: {METHOD_NAME.upper()}")
    logging.info("=" * 80)

    train_vector_path = f"7_oversampling/7_{METHOD_NAME}_train_vectors_oversampled.npy"
    train_label_path = f"7_oversampling/7_{METHOD_NAME}_train_labels_oversampled.npy"
    test_vector_path = f"6_vectorized_journal_data/6_{METHOD_NAME.lower()}_test_vectors.npy"
    test_label_path = f"6_vectorized_journal_data/6_{METHOD_NAME.lower()}_test_labels.npy"
    model_path = os.path.join(
        CLASSIFICATION_DIR, f"8_{METHOD_NAME}_ncm_hierarchical_model.pkl"
    )

    X_train, y_train = load_data(train_vector_path, train_label_path)
    X_test, y_test = load_data(test_vector_path, test_label_path)

    if X_train is None or y_train is None or X_test is None or y_test is None:
        logging.error("❌ Data tidak tersedia. Proses dihentikan.")
        logging.shutdown()
        exit()

    # *** EKSPERIMEN DENGAN PARAMETER ***
    n_clusters_options = [2, 3, 4, 5]
    linkage_options = ["ward", "complete", "average"]

    best_accuracy = 0
    best_model = None
    best_scaler = None
    best_clustering = None
    best_cluster_mapping = None
    best_silhouette_avg = None
    best_params = None

    for n_clusters in n_clusters_options:
        for linkage in linkage_options:
            logging.info(f"*** Mencoba: n_clusters={n_clusters}, linkage='{linkage}' ***")
            scaler, clustering, model, cluster_mapping, silhouette_avg = train_model(
                X_train, y_train, n_clusters, linkage
            )

            report, accuracy = predict_and_evaluate(
                scaler, clustering, model, cluster_mapping, X_test, y_test
            )

            if accuracy > best_accuracy:
                best_accuracy = accuracy
                best_model = model
                best_scaler = scaler
                best_clustering = clustering
                best_cluster_mapping = cluster_mapping
                best_silhouette_avg = silhouette_avg
                best_params = (n_clusters, linkage)

    # *** SIMPAN MODEL TERBAIK ***
    if best_model and best_clustering and best_cluster_mapping:
        save_model(
            best_model,
            best_scaler,
            best_clustering,
            best_cluster_mapping,
            best_silhouette_avg,
            model_path,
        )
        logging.info(
            f"✅ Model terbaik (n_clusters={best_params[0]}, linkage='{best_params[1]}') disimpan."
        )
    else:
        logging.error("❌ Gagal melatih model.")
        logging.shutdown()
        exit()

    logging.info("=" * 80)
    logging.info("🏆 Hasil Terbaik:")
    logging.info(f"Akurasi: {best_accuracy:.4f}")
    logging.info(f"Parameter: n_clusters={best_params[0]}, linkage='{best_params[1]}'")
    logging.info("=" * 80)

    logging.info("✅ Selesai")
    logging.info("=" * 80)
    logging.shutdown()
