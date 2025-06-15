import os
import time
import logging
import numpy as np
import joblib
from scipy.cluster.hierarchy import linkage, fcluster
from sklearn.neighbors import NearestCentroid
from sklearn.metrics import classification_report, accuracy_score, silhouette_score, confusion_matrix
from collections import Counter
from sklearn.preprocessing import StandardScaler

METHOD_NAME = "dfs"
CLASSIFICATION_DIR = "8_classification_hc_ncm"

os.makedirs(CLASSIFICATION_DIR, exist_ok=True)

LOG_FILE = os.path.join(CLASSIFICATION_DIR, f"8_{METHOD_NAME}_scipy_hierarchical_auto_improved.log")

# Konfigurasi logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(LOG_FILE), logging.StreamHandler()],
)

def load_data(vector_path, label_path):
    """Memuat data vektor dan label dari file .npy."""
    if not os.path.exists(vector_path) or not os.path.exists(label_path):
        logging.error(f"❌ File tidak ditemukan: {vector_path} atau {label_path}")
        return None, None
    try:
        X = np.load(vector_path)
        y = np.load(label_path)
        logging.info(f"✅ Data dimuat. X shape: {X.shape}, y shape: {y.shape}")
        return X, y
    except Exception as e:
        logging.error(f"❌ Gagal memuat data dari {vector_path} atau {label_path}: {e}")
        return None, None

def analyze_cluster_composition(cluster_labels, y_train):
    """Analisis komposisi label (Predator/Non-Predator) di setiap cluster."""
    cluster_composition = {}
    unique_clusters = np.unique(cluster_labels)
    logging.info(f"Analisis komposisi untuk {len(unique_clusters)} cluster.")
    for cluster_id in unique_clusters:
        # Filter label yang termasuk dalam cluster_id ini
        # Tidak perlu cek `if cluster_id in cluster_labels` karena unique_clusters sudah dari situ
        labels_in_cluster = y_train[cluster_labels == cluster_id]

        if len(labels_in_cluster) == 0:
            logging.warning(
                f"⚠️ Cluster {cluster_id} kosong! Tidak dapat menentukan label mayoritas."
            )
            cluster_composition[cluster_id] = -1  # Menandai sebagai tidak terdefinisi
            continue

        label_counts = Counter(labels_in_cluster)
        if not label_counts: # Seharusnya tidak terjadi jika len(labels_in_cluster) > 0
            logging.warning(f"⚠️ Counter label kosong untuk Cluster {cluster_id}. Melewatkan.")
            cluster_composition[cluster_id] = -1
            continue

        most_common_label = label_counts.most_common(1)[0][0]
        cluster_composition[cluster_id] = most_common_label
        logging.info(
            f"🔍 Cluster {cluster_id}: Mayoritas label = {most_common_label} (Counts: {dict(label_counts)})" # Ubah Counter ke dict untuk output log yang lebih rapi
        )

    return cluster_composition

def train_model(X_train, y_train, linkage_method, distance_threshold):
    """Melatih model dengan Hierarchical Clustering SciPy dan NCM."""
    logging.info(f"⏳ Pelatihan dimulai dengan linkage='{linkage_method}', distance_threshold={distance_threshold}...")
    start_time = time.time()

    # Preprocessing: Standardisasi Data
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    logging.info(f"✅ Data latih distandardisasi. Shape: {X_train_scaled.shape}")

    logging.info(f"🔍 Melakukan hierarchical clustering...")

    try:
        # Hitung linkage matrix
        Z = linkage(X_train_scaled, method=linkage_method)
        logging.info(f"✅ Linkage matrix dihitung. Shape: {Z.shape}")

        # Membuat cluster dengan memotong dendrogram pada distance_threshold
        cluster_labels = fcluster(Z, t=distance_threshold, criterion='distance')

        # Ubah label cluster agar mulai dari 0 (opsional, fcluster biasanya mulai dari 1)
        # Ini penting jika Anda ingin label kluster konsisten (0-indexed)
        if cluster_labels.min() == 1:
             cluster_labels = cluster_labels - 1

        num_clusters = len(np.unique(cluster_labels))
        logging.info(f"✅ Clustering selesai. Jumlah cluster yang terbentuk: {num_clusters}")

        # Handle kasus jika hanya ada 1 cluster
        if num_clusters <= 1:
            logging.warning(f"⚠️ Hanya terbentuk {num_clusters} cluster dengan parameter ini. Melewatkan NCM dan evaluasi.")
            return scaler, Z, None, {}, -1, False # Menambahkan flag success = False

        # Hitung silhouette score
        try:
            # Periksa apakah ada setidaknya 2 cluster (untuk silhouette_score)
            if num_clusters > 1:
                silhouette_avg = silhouette_score(X_train_scaled, cluster_labels)
                logging.info(f"📊 Silhouette Score: {silhouette_avg:.4f}")
            else:
                silhouette_avg = -1 # Tidak dapat menghitung jika hanya 1 cluster
                logging.warning("⚠️ Tidak dapat menghitung silhouette score karena hanya ada 1 cluster.")
        except Exception as e:
            logging.warning(f"⚠️ Gagal menghitung silhouette score: {e}")
            silhouette_avg = -1

        # Analisis komposisi cluster
        cluster_mapping = analyze_cluster_composition(cluster_labels, y_train)

        # Handle kasus jika cluster_mapping kosong
        if not cluster_mapping:
             logging.warning("⚠️ Cluster mapping kosong. Tidak dapat melatih NCM.")
             return scaler, Z, None, cluster_mapping, silhouette_avg, False

        # Melatih Nearest Centroid Classifier
        logging.info("🧠 Melatih Nearest Centroid Classifier berdasarkan cluster hasil clustering...")
        clf = NearestCentroid(metric="euclidean")
        clf.fit(X_train_scaled, cluster_labels) # Melatih NCM dengan data scaled dan label cluster
        logging.info("✅ NCM Classifier selesai dilatih.")

        training_time = time.time() - start_time
        logging.info(f"⏳ TOTAL WAKTU PELATIHAN: {training_time:.2f} detik")

        return scaler, Z, clf, cluster_mapping, silhouette_avg, True

    except Exception as e:
        logging.error(f"❌ Terjadi kesalahan selama pelatihan: {e}")
        return scaler, None, None, {}, -1, False

def predict_and_evaluate(scaler, clf, cluster_mapping, X_test, y_test, y_train_global):
    """
    Memprediksi dan mengevaluasi model.
    Menambahkan y_train_global untuk mendapatkan label mayoritas global.
    """
    logging.info("📌 Memulai prediksi dan evaluasi...")
    start_time = time.time()

    # Preprocessing data uji dengan scaler yang sama
    if scaler:
        X_test_scaled = scaler.transform(X_test)
        logging.info("✅ Data uji distandardisasi.")
    else:
        X_test_scaled = X_test
        logging.warning("⚠️ Scaler tidak tersedia. Menggunakan data uji asli.")


    if clf is None or cluster_mapping is None:
        logging.error("❌ Classifier atau cluster mapping tidak tersedia untuk prediksi.")
        return None, None, None


    try:
        # Prediksi label cluster menggunakan NCM
        cluster_labels_pred = clf.predict(X_test_scaled)

        # Mapping label cluster ke label kelas asli
        y_pred = np.array(
            [cluster_mapping.get(cluster_id, -1) for cluster_id in cluster_labels_pred]
        )

        # Menangani cluster_id yang tidak terdefinisi dalam mapping (-1)
        if -1 in y_pred:
            logging.warning(
                "⚠️ Terdapat cluster yang tidak terdefinisi dalam mapping (label -1). "
                "Menetapkan label mayoritas global dari data latih."
            )
            try:
                # Menggunakan y_train_global untuk mendapatkan kelas mayoritas
                most_frequent_class_global = Counter(y_train_global).most_common(1)[0][0]
                y_pred[y_pred == -1] = most_frequent_class_global
                logging.info(f"✅ Label -1 diganti dengan label mayoritas global: {most_frequent_class_global}")
            except Exception as e:
                logging.error(f"❌ Gagal menghitung label mayoritas global: {e}. Menggunakan default 0.")
                y_pred[y_pred == -1] = 0 # Default ke kelas 0 jika gagal

        # Evaluasi model
        report = classification_report(
            y_test,
            y_pred,
            target_names=["Non-Predator", "Predator"],
            digits=4,
            zero_division=0,
        )
        accuracy = accuracy_score(y_test, y_pred)
        cm = confusion_matrix(y_test, y_pred)

        logging.info("📊 Laporan Klasifikasi:\n%s", report)
        logging.info(f"🎯 Akurasi: {accuracy:.4f}")
        logging.info("📊 Confusion Matrix:\n%s", cm)

        evaluation_time = time.time() - start_time
        logging.info(f"⏳ Waktu Evaluasi: {evaluation_time:.2f} detik")

        return report, accuracy, cm

    except Exception as e:
        logging.error(f"❌ Terjadi kesalahan selama prediksi atau evaluasi: {e}")
        return None, None, None

def save_model(model, scaler, linkage_matrix, cluster_mapping, silhouette_avg, model_path):
    """Menyimpan model dan artefak terkait."""
    try:
        # Pastikan linkage_matrix adalah array numpy sebelum disimpan
        if isinstance(linkage_matrix, np.ndarray):
            joblib.dump((model, scaler, linkage_matrix, cluster_mapping, silhouette_avg), model_path)
            logging.info(
                f"✅ Model, scaler, linkage matrix, cluster_mapping, dan silhouette score disimpan ke {model_path}"
            )
        else:
            logging.error(f"❌ linkage_matrix bukan numpy array, tidak dapat disimpan: {type(linkage_matrix)}")
    except Exception as e:
        logging.error(f"❌ Gagal menyimpan model ke {model_path}: {e}")


def load_model(model_path):
    """Memuat model dan artefak terkait."""
    try:
        model, scaler, linkage_matrix, cluster_mapping, silhouette_avg = joblib.load(
            model_path
        )
        logging.info(
            f"✅ Model, scaler, linkage matrix, cluster_mapping, dan silhouette score dimuat dari {model_path}"
        )
        return model, scaler, linkage_matrix, cluster_mapping, silhouette_avg
    except FileNotFoundError:
        logging.error(f"❌ File model tidak ditemukan di {model_path}")
        return None, None, None, None, None
    except Exception as e:
        logging.error(f"❌ Gagal memuat model dari {model_path}: {e}")
        return None, None, None, None, None

if __name__ == "__main__":
    logging.info("=" * 80)
    logging.info(f"🚀 MULAI TRAINING MODEL IMPROVED: {METHOD_NAME.upper()}")
    logging.info("=" * 80)

    # Jalur file data
    train_vector_path = f"7_oversampling/7_{METHOD_NAME}_train_vectors_oversampled.npy"
    train_label_path = f"7_oversampling/7_{METHOD_NAME}_train_labels_oversampled.npy"
    test_vector_path = f"6_vectorized_journal_data/6_{METHOD_NAME.lower()}_test_vectors.npy"
    test_label_path = f"6_vectorized_journal_data/6_{METHOD_NAME.lower()}_test_labels.npy"
    # Menggunakan CLASSIFICATION_DIR yang baru
    model_path = os.path.join(
        CLASSIFICATION_DIR, f"8_{METHOD_NAME}_scipy_hierarchical_auto_improved_model.pkl"
    )

    # Memuat data
    X_train, y_train = load_data(train_vector_path, train_label_path)
    X_test, y_test = load_data(test_vector_path, test_label_path)

    if X_train is None or y_train is None or X_test is None or y_test is None:
        logging.error("❌ Data tidak tersedia. Proses dihentikan.")
        logging.shutdown()
        exit()

    # Parameter tuning options
    linkage_methods = ["ward", "average", "complete"]
    # Menambahkan rentang distance_threshold yang lebih luas dan lebih granular
    distance_threshold_options = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
    # Anda mungkin perlu menyesuaikan rentang ini berdasarkan distribusi jarak di data Anda

    best_accuracy = 0
    best_model = None
    best_scaler = None
    best_linkage = None
    best_cluster_mapping = None
    best_silhouette_avg = -1 # Inisialisasi dengan -1 karena silhouette_score bisa negatif
    best_distance_threshold = None
    best_linkage_method = None
    best_report = None
    best_cm = None

    # Loop melalui semua kombinasi parameter
    for linkage_method in linkage_methods:
        for distance_threshold in distance_threshold_options:
            logging.info("=" * 60)
            logging.info(f"*** Mencoba linkage='{linkage_method}', distance_threshold={distance_threshold} ***")

            # Melatih model
            scaler, linkage_matrix, model, cluster_mapping, silhouette_avg, training_success = train_model(
                X_train, y_train, linkage_method=linkage_method, distance_threshold=distance_threshold
            )

            if not training_success:
                logging.warning("⚠️ Pelatihan tidak berhasil untuk parameter ini. Melewatkan evaluasi.")
                continue

            # Memprediksi dan mengevaluasi
            # Mengirimkan y_train agar `predict_and_evaluate` dapat menghitung mayoritas global
            report, accuracy, cm = predict_and_evaluate(
                scaler, model, cluster_mapping, X_test, y_test, y_train # Ditambahkan
            )

            # Membandingkan dan menyimpan model terbaik
            # Pastikan akurasi valid (tidak None)
            if accuracy is not None and accuracy > best_accuracy:
                best_accuracy = accuracy
                best_model = model
                best_scaler = scaler
                best_linkage = linkage_matrix
                best_cluster_mapping = cluster_mapping
                best_silhouette_avg = silhouette_avg
                best_distance_threshold = distance_threshold
                best_linkage_method = linkage_method
                best_report = report
                best_cm = cm

    # Simpan model terbaik
    if best_model is not None and best_scaler is not None and best_linkage is not None and best_cluster_mapping is not None:
        save_model(
            best_model,
            best_scaler,
            best_linkage,
            best_cluster_mapping,
            best_silhouette_avg,
            model_path,
        )
        logging.info(
            f"✅ Model terbaik (linkage='{best_linkage_method}', distance_threshold={best_distance_threshold}) disimpan."
        )
    else:
        logging.error("❌ Gagal menemukan model terbaik yang valid untuk disimpan.")


    logging.info("=" * 80)
    logging.info("🏆 Hasil Terbaik dari Semua Eksperimen:")
    if best_model is not None:
        logging.info(f"Akurasi: {best_accuracy:.4f}")
        logging.info(f"Parameter Terbaik: linkage='{best_linkage_method}', distance_threshold={best_distance_threshold}")
        logging.info(f"Silhouette Score (Train): {best_silhouette_avg:.4f}") # Menampilkan silhouette score
        if best_report:
             logging.info("📊 Laporan Klasifikasi Model Terbaik:\n%s", best_report)
        if best_cm is not None:
             logging.info("📊 Confusion Matrix Model Terbaik:\n%s", best_cm)

    else:
        logging.info("❌ Tidak ada model terbaik yang berhasil dilatih dan dievaluasi.")

    logging.info("=" * 80)
    logging.info("✅ Proses Selesai")
    logging.info("=" * 80)
    logging.shutdown()
